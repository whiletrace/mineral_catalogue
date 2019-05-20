import string

from django import template

register = template.Library()


@register.inclusion_tag('trace_minerals/glossary_filter.html')
def glossary_filter(**kwargs):
    """ responsible for outputting ASCII uppercase alphabet

    this is outputted to Glossary_filter.html
    :param **kwargs
    :type dict
    :var glossary
    :type str
    :return dict
    """
    glossary = string.ascii_uppercase

    return {'glossary':glossary, 'current_letter':kwargs['current_letter']}
