
# Custom Model-From in django-admin demo 
Q:
class Person(Model):
  first_name = CharField(...)
  last_name = CharField(...)
  def name():
    return first_name + ' ' + last_name
'''
    Displaying the name as a single column in the admin change list is easy enough. However, 
    I need a single, editable "name" field that is editable from the list page, 
    which I can then parse to extract and set the model field values. The parsing isn't a concern. 
    I am just wondering how to have an editable form field on the list page 
    that doesn't correspond directly to a model field.
'''

A:
class PersonChangeListForm(forms.ModelForm):
    class Meta:
        model = Person
    name = forms.CharField()

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        if instance:
            initial = kwargs.get('initial', {})
            initial['name'] = '%s %s' % (instance.first_name, instance.last_name)
            kwargs['initial'] = initial
        super(PersonChangeListForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        # use whatever parsing you like here
        first_name, last_name = self.cleaned_data['name'].split(None, 1)
        self.cleaned_data['first_name'] = first_name
        self.cleaned_data['last_name'] = last_name
        super(PersonChangeListForm, self).save(*args, **kwargs)

class PersonAdmin(admin.ModelAdmin):
    def get_changelist_form(self, request, **kwargs):
        return PersonChangeListForm

