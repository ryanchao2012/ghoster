from django import forms
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.forms.utils import flatatt
from django.utils.encoding import force_text
from django.forms.widgets import ChoiceInput
class GhosterTextInputWidget(forms.TextInput):
    def __init__(self, attrs=None):
        final_attrs = {'class': 'form-control'}
        if attrs is not None:
            final_attrs.update(attrs)
        super(GhosterTextInputWidget, self).__init__(attrs=final_attrs)


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
        import inspect
        print(inspect.stack())
        if 'id' in final_attrs:
            final_attrs.update({'class': 'switch-input'})
            return format_html('<label class="switch switch-icon switch-pill switch-primary"><input{} /><span class="switch-label" data-on="&#xF00C;" data-off="&#xF00D;"></span><span class="switch-handle"></span></label>', flatatt(final_attrs))
        return format_html('<input{} />', flatatt(final_attrs))
