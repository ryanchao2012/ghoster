from django.contrib import admin
from .models import Post, Editor, Category, Menu, Page
from .widgets import GhCheckboxInput
from .forms import GhosterPostForm, GhosterMetaForm
from django.forms import CheckboxSelectMultiple
from django.db import models
class PostAdmin(admin.ModelAdmin):
    list_display = ('short_title', 'image_thumb', 'editor', 'page', 'category', 'date', 'publish')
    list_editable = ('page', 'category', 'publish')
    search_fields = ('tags__name', 'editor__name',)
    list_filter = ('page__title', 'editor__name')
    change_form_template = 'admin/ghoster_change_form.html'
    add_form_template = 'admin/ghoster_change_form.html'

    def get_changelist_form(self, request, **kwargs):
        return GhosterPostForm



class EditorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


# Register your models here.



admin.site.register(Post, PostAdmin)
admin.site.register(Editor, EditorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Page, PageAdmin)
