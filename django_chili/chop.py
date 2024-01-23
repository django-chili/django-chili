import ast

from django import template

from django_chili.sauce import Sauce


class ChopNode(template.Node):
    tag = "chop"

    def __init__(self, content_node, match, target="tag", attr=None):
        self.content_node = content_node
        self.match = match
        self.target = target
        self.attr = attr

    def render(self, context):
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
