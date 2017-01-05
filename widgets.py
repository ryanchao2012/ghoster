from django import forms


class GhosterTextInputWidget(forms.TextInput):
    def __init__(self, attrs=None):
        final_attrs = {'class': 'form-control'}
        if attrs is not None:
            final_attrs.update(attrs)
        super(GhosterTextInputWidget, self).__init__(attrs=final_attrs)




