from django.utils.safestring import mark_safe


def chunk_tag(context):
    """
    Process the given context and return the HTML tag as a safe string.

    :param context: A dictionary containing the context data.
    :type context: dict

    :return: The HTML tag as a safe string.
    :rtype: safe string
    """
    tag = context['tag']
    html = str(tag)
    return mark_safe(html)
