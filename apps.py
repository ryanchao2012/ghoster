from django.apps import AppConfig
from django.conf import settings
from django import db
from django.forms.widgets import Select, CheckboxInput
from django.contrib.admin import options
from .widgets import GhosterTextInputWidget, GhosterWidget
    # GhosterURLFieldWidget




class GhosterConfig(AppConfig):
    name = 'ghoster'
    verbose_name = "GHOSTER CMS"
    settings.TEMPLATES[0]['OPTIONS']['context_processors'].append('ghoster.context_processors.application')
    Select.render = GhosterWidget.select_render
    CheckboxInput.render = GhosterWidget.slider_checkbox_render
    options.FORMFIELD_FOR_DBFIELD_DEFAULTS[db.models.CharField].update({'widget': GhosterTextInputWidget})

    # options.FORMFIELD_FOR_DBFIELD_DEFAULTS[db.models.CharField]['widget'] = GhosterTextInputWidget




