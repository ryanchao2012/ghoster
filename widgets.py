from django import forms
from django.forms import ClearableFileInput
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.forms.utils import flatatt
from django.utils.encoding import force_text
from django.forms.widgets import CheckboxInput
from django.utils.html import conditional_escape
from django.utils.html import smart_urlquote
from django.utils.translation import ugettext as _

class GhosterTextInputWidget(forms.TextInput):
    def __init__(self, attrs=None):
        final_attrs = {'class': 'form-control'}
        if attrs is not None:
            final_attrs.update(attrs)
        super(GhosterTextInputWidget, self).__init__(attrs=final_attrs)



class GhosterURLFieldWidget(ClearableFileInput):
    template_default = (
        '<div class="btn btn-primary btn-block">'
        '<i class="fa fa-cloud-upload fa-lg">%(input)s</i>'
        '</div>'
    )
    template_with_initial = (
        '<img src="%(initial_url)s" width="200" /><br />'
        + template_default +
        '%(clear_template)s'
        # '<p class="file-upload">%s</p>' % forms.ClearableFileInput.template_with_initial
    )
    template_with_clear = (
        '%s' % forms.ClearableFileInput.template_with_clear
    )

    def render(self, name, value, attrs=None):
        substitutions = {
            'initial_text': self.initial_text,
            'input_text': self.input_text,
            'clear_template': '',
            'clear_checkbox_label': self.clear_checkbox_label,
        }
        template = GhosterURLFieldWidget.template_default
        substitutions['input'] = super(ClearableFileInput, self).render(name, value, attrs)

        if self.is_initial(value):
            template = self.template_with_initial
            substitutions.update(self.get_template_substitution_values(value))
            if not self.is_required:
                checkbox_name = self.clear_checkbox_name(name)
                checkbox_id = self.clear_checkbox_id(checkbox_name)
                substitutions['clear_checkbox_name'] = conditional_escape(checkbox_name)
                substitutions['clear_checkbox_id'] = conditional_escape(checkbox_id)
                substitutions['clear'] = CheckboxInput().render(checkbox_name, False, attrs={'id': checkbox_id})
                substitutions['clear_template'] = self.template_with_clear % substitutions
        return mark_safe(template % substitutions)

class GhosterWidget(object):

    @staticmethod
    def select_render(self, name, value, attrs=None):
        if value is None:
            value = ''
        attrs.update({'class': 'form-control'}) #
        final_attrs = self.build_attrs(attrs, name=name)
        output = [format_html('<select{}>', flatatt(final_attrs))]
        options = self.render_options([value])
        if options:
            output.append(options)
        output.append('</select>')
        return mark_safe('\n'.join(output))

    @staticmethod
    def slider_checkbox_render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, type='checkbox', name=name)

        if self.check_test(value):
            final_attrs['checked'] = 'checked'
        if not (value is True or value is False or value is None or value == ''):
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(value)
        if 'id' in final_attrs:
            final_attrs.update({'class': 'switch-input'})
            return format_html('<label class="switch switch-icon switch-pill switch-primary"><input{} /><span class="switch-label" data-on="&#xF00C;" data-off="&#xF00D;"></span><span class="switch-handle"></span></label>', flatatt(final_attrs))
        return format_html('<input{} />', flatatt(final_attrs))
