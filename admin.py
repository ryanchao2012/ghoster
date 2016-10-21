from django.contrib import admin
from .models import Post, Editor, Category, Menu, Page, Tag

from django.forms import CheckboxSelectMultiple
from django.db import models
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'editor', 'image_thumb', 'page', 'category', 'date')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('editor', 'tag')
    search_fields = ('tag__name', 'editor__name',)
    raw_id_fields = ('tag',)
    change_form_template = 'admin/ghoster_change_form.html'
    add_form_template = 'admin/ghoster_change_form.html'

class EditorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


# Register your models here.



admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Editor, EditorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Page, PageAdmin)
