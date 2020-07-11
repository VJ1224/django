from django import template
import mistune

register = template.Library()
print(mistune)

@register.filter
def markdown(value):
    markdown = mistune.Markdown()
    return markdown(value)