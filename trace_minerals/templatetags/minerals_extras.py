import string

from django import template

register = template.Library()


@register.inclusion_tag('trace_minerals/glossary_filter.html')
def glossary_filter():
    glossary = string.ascii_lowercase

    return {'glossary':glossary}
