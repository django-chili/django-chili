from django import template

from django_chili.bowl import bowl_tag, BowlNode
from django_chili.chop import chop_tag, ChopNode
from django_chili.chunk import chunk_tag

register = template.Library()

register.tag(compile_function=bowl_tag, name=BowlNode.tag)
register.tag(compile_function=chop_tag, name=ChopNode.tag)
register.simple_tag(func=chunk_tag, takes_context=True, name="chunk", )
