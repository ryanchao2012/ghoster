from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from datetime import datetime
# Create your models here.



class Editor(models.Model):
    name = models.CharField(max_length = 31)
    brief = models.CharField(max_length = 255, blank = True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = _('EDITOR')
        verbose_name_plural = verbose_name

class Category(models.Model):
    name = models.CharField(max_length=31)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = _('CATEGORY')
        verbose_name_plural = verbose_name

class Menu(models.Model):
    name = models.CharField(max_length = 31)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = _('MENU')
        verbose_name_plural = verbose_name

class Page(models.Model):
    title = models.CharField(max_length = 255)
    subtitle = models.CharField(max_length = 255, blank = True)

    menu = models.ForeignKey(Menu, default = 1)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = _('PAGE')
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=31)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = _('TAG')
        verbose_name_plural = verbose_name


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, allow_unicode=True)
    content = models.TextField()
    thumbnail = models.URLField(blank=True)
    editor = models.ForeignKey(Editor, default=1)
    category = models.ForeignKey(Category, default=1)
    page = models.ForeignKey(Page, default=1)
    date = models.DateTimeField(default=datetime.now)
    tag = models.ManyToManyField(Tag, blank=True)

    def image_thumb(self):
        return '<img src="%s" height="100" />' % (self.thumbnail)

    image_thumb.allow_tags = True

    @permalink
    def get_absolute_url(self):
        return reverse('single_post', args={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = _('POST')
        verbose_name_plural = verbose_name

