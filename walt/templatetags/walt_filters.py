from django import template
from datetime import datetime

register = template.Library()

@register.filter
def plusify(value):
    return value.replace(" ", '+')

@register.filter
def only_date(value):
    return value[:10]