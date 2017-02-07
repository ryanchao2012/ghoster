from django import template
from ghoster import forms
from django.contrib import admin
from django.contrib.admin import helpers
import pprint
import copy
import re
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
            (name, {'fields': flatten(opts['fields'])})
        )
    return flat


def get_meta_fieldsets(flat_fieldsets, model_admin):
    markdown_field_name = model_admin.markdown_field
    title_field_name = model_admin.title_field
    meta_fieldsets = []
    has_markdown = False
    has_title = False
    for name, opts in flat_fieldsets:
        if not has_markdown:
            if markdown_field_name in opts['fields']:
                opts['fields'].remove(markdown_field_name)
                has_markdown = True

        if not has_title:
            if title_field_name in opts['fields']:
                opts['fields'].remove(title_field_name)
                has_title = True

        meta_fieldsets.append(
            (name, {'fields': opts['fields']})
        )
    return meta_fieldsets

@register.simple_tag
def get_base_media():
    pass
    # return forms.BaseMadiaWidget().media


@register.simple_tag(takes_context=True)
def get_gh_app_list(context):
    return admin.site.get_app_list(context['request'])

@register.simple_tag()
def get_ghoster_form(adminform):
    form = adminform.form
    model_admin = adminform.model_admin
    readonly_fields = adminform.readonly_fields
    flat_fieldsets = flatten_fieldsets(adminform.fieldsets)
    prepopulated_fields = adminform.prepopulated_fields
    if prepopulated_fields:
        prepopulated_fields = prepopulated_fields[0]
    else: 
        prepopulated_fields = {}

    meta_fieldsets = get_meta_fieldsets(flat_fieldsets, model_admin)

    markdownfield = form[model_admin.markdown_field]
    markdownfield.id = re.search(r'id=\"(\S+)\"', str(markdownfield)).group(1)
    
    titlefield = form[model_admin.title_field]
    titlefield.field.widget.attrs['class'] += ' form-control'
    
    metaformsets = helpers.AdminForm(
        form, 
        meta_fieldsets, 
        prepopulated_fields, 
        readonly_fields=readonly_fields, 
        model_admin=model_admin
    )

    return {'markdown': markdownfield, 'title': titlefield, 'meta': metaformsets}


