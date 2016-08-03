from django import forms

class BaseMadiaWidget(forms.TextInput):
    class Media:
        css = {
            'all': ('admin/css/base.css',
                    'admin/css/bootstrap.css',
                    'admin/css/fonts.css',
                    )
        }
        js = ('admin/js/collapse.js',
              'admin/js/actions.js'
              )