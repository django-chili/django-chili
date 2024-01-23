from django import template
from django.utils.safestring import mark_safe

from django_chili.sauce import Sauce


class BowlNode(template.Node):
    tag = 'bowl'

    def __init__(self, content_node, filename):
        self.content_node = content_node

        with open(filename, 'r') as file:
            self.contents = file.read()

    def render(self, context):
        sauce = Sauce(self.contents)
        context['sauce'] = sauce
        self.content_node.render(context)
        html = str(sauce)
        return mark_safe(html)


def bowl_tag(parser, token):
    tag_name, filename = token.contents.split(None, 1)
    content_node = parser.parse((f'end{BowlNode.tag}',))
    parser.delete_first_token()
    return BowlNode(content_node, filename.strip())
