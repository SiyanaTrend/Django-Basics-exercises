from django import template

register = template.Library()


@register.filter
def split_by_comma_space(value):
    # return value.split(", ")
    return [item.strip() for item in value.split(",")]
