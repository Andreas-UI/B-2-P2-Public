# blog/templatetags/markdown_extras.py
from django import template
from django.template.defaultfilters import stringfilter

from pawn.utils import markdownify

register = template.Library()

@register.filter()
@stringfilter

def markdown(value):
    return markdownify(value)

@register.filter
def cool_number(value, num_decimals=2):
    """
    Django template filter to convert regular numbers to a
    cool format (ie: 2K, 434.4K, 33M...)
    :param value: number
    :param num_decimals: Number of decimal digits
    """

    int_value = int(value)
    formatted_number = '{{:.{}f}}'.format(num_decimals)
    if int_value < 1000:
        return str(int_value)
    elif int_value < 1000000:
        return formatted_number.format(int_value/1000.0).rstrip('0.') + 'k'
    else:
        return formatted_number.format(int_value/1000000.0).rstrip('0.') + 'M'