from django import forms
from .models import Post
from django.contrib.admin.helpers import AdminForm
from django.contrib.admin.widgets import AdminSplitDateTime
class BaseMadiaWidget(forms.TextInput):
    class Media:
        css = {
            'all': (
                    'admin/css/bootstrap.css',
                    'open-iconic/font/css/open-iconic-bootstrap.css',
                    'admin/vendor/animo/animate+animo.css',
                    'admin/vendor/fontawesome/css/font-awesome.min.css',
                    'admin/vendor/csspinner/csspinner.min.css',
                    'admin/css/base.css',
                    'admin/css/app.css',
                    )
        }
        js = (
              'admin/vendor/modernizr/modernizr.js',
              'admin/vendor/fastclick/fastclick.js',
              'admin/vendor/jquery/jquery.min.js',
              'admin/vendor/bootstrap/js/bootstrap.min.js',
              'admin/vendor/animo/animo.min.js',
              'admin/js/app.js'
              )


# class GhosterPostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         exclude = []
#         widgets = {
#             'date': AdminSplitDateTime(),
#         }


class GhosterContentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']

class GhosterMetaForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['content']
        widgets = {
            'date': AdminSplitDateTime(),
        }

    def __init__(self, *args, **kwargs):
        super(GhosterMetaForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Untitled'})
        self.fields['slug'].widget.attrs.update({'class': 'form-control'})
        self.fields['thumbnail'].widget.attrs.update({'class': 'form-control'})
        # self.fields['category'].widget.attrs.update({'class': 'form-control'})


