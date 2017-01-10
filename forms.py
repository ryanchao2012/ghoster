from django import forms
from .models import Post
from django.contrib.admin.helpers import AdminForm
from django.contrib.admin.widgets import AdminSplitDateTime
from .widgets import (
    GhFileFieldWidget, GhTagInputWidget,
    GhCheckboxInput, GhTextInputWidget,
)

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

class GhosterPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = []
        widgets = {
            'title': GhTextInputWidget(),
            'slug': GhTextInputWidget(),
            'date': AdminSplitDateTime(),
            'cover': GhFileFieldWidget(),
            'tags': GhTagInputWidget(),
            'publish': GhCheckboxInput(),
        }

class GhosterContentForm(forms.ModelForm):
    class Meta(GhosterPostForm.Meta):
        fields = ['content']

class GhosterMetaForm(forms.ModelForm):
    class Meta(GhosterPostForm.Meta):
        exclude = ['content']

    def __init__(self, *args, **kwargs):
        super(GhosterMetaForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Untitled'})


