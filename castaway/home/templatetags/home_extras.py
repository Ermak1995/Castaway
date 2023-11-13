from django import template

register = template.Library()


@register.simple_tag
def show_value(d: dict, key):
    return d[key]
