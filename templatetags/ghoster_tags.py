from django import template
from ghoster import forms

register = template.Library()

@register.simple_tag
def get_base_media():
    return forms.BaseMadiaWidget().media


@register.simple_tag
def render_post_form(post):
    content = forms.GhosterContentForm(instance = post)
    meta = forms.GhosterMetaForm(instance = post)
    return {'content': content['content'], 'meta': meta}

