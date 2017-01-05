from django.apps import AppConfig
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.forms.utils import flatatt
from django.forms.widgets import Select
from django.contrib.admin import options
from .widgets import GhosterTextInputWidget


def gh_render(self, name, value, attrs=None):
    if value is None:
        value = ''
    attrs.update({'class': 'form-control'})
    final_attrs = self.build_attrs(attrs, name=name)
    output = [format_html('<select{}>', flatatt(final_attrs))]
    options = self.render_options([value])
    if options:
        output.append(options)
    output.append('</select>')
    return mark_safe('\n'.join(output))

class GhosterConfig(AppConfig):
    name = 'ghoster'
    verbose_name = "GHOSTER CMS"
    settings.TEMPLATES[0]['OPTIONS']['context_processors'].append('ghoster.context_processors.application')
    Select.render = gh_render
    # options.FORMFIELD_FOR_DBFIELD_DEFAULTS[db.models.CharField]['widget'] = GhosterTextInputWidget




