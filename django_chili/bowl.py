from django import template
from django.utils.safestring import mark_safe

from django_chili.sauce import Sauce


class BowlNode(template.Node):
    """

    This class represents a custom template node for rendering a Bowl.

        - `BowlNode` is a subclass of `template.Node`.

    Attributes:
        - `tag` (str): Represents the tag name used in the template for this node.

    Methods:
        - `__init__(self, content_node: template.Node, filename: str)`:
            Initializes a new `BowlNode` instance with the given `content_node` and `filename`. The `content_node` represents the content of the node in the template, and the `filename`
    * is a string representing the path to the file containing the contents of the bowl.

        - `render(self, context: template.Context) -> str`:
            Renders the `BowlNode` by reading the contents of the file specified by `filename` and creating a `Sauce` instance with the contents. The `Sauce` instance is then added to the
    * context as a variable named 'sauce'. The `content_node` is then rendered in the provided context. Finally, the `str` representation of the `Sauce` instance is returned as HTML.

    """
    tag = 'bowl'

    def __init__(self, content_node, filename):
        self.content_node = content_node

        with open(filename, 'r') as file:
            self.contents = file.read()

    def render(self, context):
        """
        Render Method

        This method is used to render the contents of a Sauce instance with the provided context.

        :param context: The context dictionary containing the values to be rendered.

        :return: The rendered HTML as a string.

        """
        sauce = Sauce(self.contents)
        context['sauce'] = sauce
        self.content_node.render(context)
        html = str(sauce)
        return mark_safe(html)


def bowl_tag(parser, token):
    """
    :param parser: The Django template parser object.
    :param token: The Django template token object.
    :return: A BowlNode object.

    This method is a custom template tag for the Django templating engine. It takes two parameters, `parser` which is the template parser object, and `token` which is the template token
    * object. It performs a specific logic to parse the tag name and filename from the token contents, then parses the content nodes using the parser, deletes the first token, and returns
    * a BowlNode object with the parsed content node and stripped filename.
    """
    tag_name, filename = token.contents.split(None, 1)
    content_node = parser.parse((f'end{BowlNode.tag}',))
    parser.delete_first_token()
    return BowlNode(content_node, filename.strip())
