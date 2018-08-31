from django.template import Library
from datetime import datetime

register = Library()

@register.filter(name='split')
def split(value, key):
    return value.split(key)