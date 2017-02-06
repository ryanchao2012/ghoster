from django import template
from ghoster import forms
from django.contrib import admin
import pprint
# from django.contrib.admin.utils import flatten_fieldsets

register = template.Library()


def flatten(fields):
    """Returns a list which is a single level of flattening of the
    original list."""
    flat = []
    for field in fields:
        if isinstance(field, (list, tuple)):
            flat.extend(field)
        else:
            flat.append(field)
    return flat

def flatten_fieldsets(fieldsets):
    """Returns a list of field names from an admin fieldsets structure."""
    flat = []
    for name, opts in fieldsets:
        flat.append(
            (name, {'fields': tuple(flatten(opts['fields']))})
        )
    return flat

@register.simple_tag
def get_base_media():
	pass
    # return forms.BaseMadiaWidget().media


@register.simple_tag(takes_context=True)
def get_gh_app_list(context):
	return admin.site.get_app_list(context['request'])

@register.simple_tag
def render_post_form(adminform):
	adminform.fieldsets = flatten_fieldsets(adminform.fieldsets)
	pprint.pprint(adminform.__dict__, width=1)
	return adminform
	# for fieldset in adminform:
	# 	print('---fieldset---')
	# 	pprint.pprint(fieldset.__dict__, width=1)
	# 	for line in fieldset:
	# 		print('--line--')
	# 		pprint.pprint(line.__dict__, width=1)
	# 		for field in line:
	# 			print('@')
	# 			pprint.pprint(field.__dict__, width=1)

	# pprint.pprint(form.form.fields['char_field'].widget, width=1)
	
#     content = forms.GhosterContentForm(instance = post)
#     meta = forms.GhosterMetaForm(instance = post)
#     return {'content': content['content'], 'meta': meta}

