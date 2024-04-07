from django import template


register = template.Library()

@register.filter(name='tags')
def tags(quote_tags):
    return quote_tags.all()

