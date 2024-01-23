import ast

from django import template

from django_chili.sauce import Sauce


class ChopNode(template.Node):
    """
    Represents a custom template tag node that allows chopping and manipulating HTML tags.

    Args:
        content_node (Node): The node containing the content to be rendered.
        match (str): The CSS selector used to find the tags to be manipulated.
        target (str, optional): The target of the manipulation. Default is "tag".
        attr (str, optional): The attribute name to be modified. Required only if target is "attr".

    Attributes:
        tag (str): The name of the custom template tag.

    Methods:
        render(context): Renders the custom template tag node.

    """
    tag = "chop"

    def __init__(self, content_node, match, target="tag", attr=None):
        self.content_node = content_node
        self.match = match
        self.target = target
        self.attr = attr

    def render(self, context):
        """
        Renders the content based on the given context.

        :param context: The context containing the data.
        :type context: dict
        :return: The rendered content.
        :rtype: str
        """
        tags = context['sauce'].select(self.match)

        for tag in tags:
            context['tag'] = tag
            content = self.content_node.render(context)
            content = str(content)
            content_tag = Sauce(content)

            match self.target:
                case "tag":
                    tag.replace_with(content_tag)
                case "inner":
                    tag.clear()
                    tag.append(content_tag)
                case "attr":
                    tag.attrs.pop(self.attr)
                    tag.attrs.update({self.attr: content_tag})

        return ""


def chop_tag(parser, token):
    """
    :param parser: The parser object used for parsing the template.
    :param token: The tag's token string.
    :return: The parsed ChopNode object.

    This method takes a parser object and a token string as input parameters and returns a parsed ChopNode object.

    The method works by splitting the token string into the tag name and arguments. It then processes the arguments by splitting them further into positional arguments and named arguments
    *. Positional arguments are added to a list while named arguments are added to a dictionary.

    After processing the arguments, the method calls the parser to parse the content node using the 'endChopNode' tag as the end point. It then deletes the first token and returns a Chop
    *Node object created from the parsed content node and the positional and named arguments.
    """
    tag_name, args = token.contents.split(None, 1)

    parts = args.split(',')

    positional_arguments = []
    named_arguments = {}

    for part in parts:
        arg = part.strip().split('=')

        if len(arg) == 1:
            positional_arguments.append(ast.literal_eval(arg[0].strip()))
        elif len(arg) == 2:
            named_arguments[arg[0]] = ast.literal_eval(arg[1].strip())

    content_node = parser.parse((f'end{ChopNode.tag}',))
    parser.delete_first_token()
    return ChopNode(content_node, *positional_arguments, **named_arguments)
