from django import forms

class BaseMadiaWidget(forms.TextInput):
    class Media:
        css = {
            'all': (
                    'admin/css/bootstrap.css',
                    'admin/vendor/fontawesome/css/font-awesome.min.css',
                    'admin/vendor/animo/animate+animo.css',
                    'admin/vendor/csspinner/csspinner.min.css',
                    'admin/css/app.css',
                    'admin/css/base.css',
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

