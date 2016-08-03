from django import template
from ghoster import forms

register = template.Library()

@register.simple_tag
def get_base_media():
    return forms.BaseMadiaWidget().media
