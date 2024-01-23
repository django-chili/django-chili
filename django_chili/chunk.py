from django.utils.safestring import mark_safe


def chunk_tag(context):
    tag = context['tag']
    html = str(tag)
    return mark_safe(html)
