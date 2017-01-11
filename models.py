from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from datetime import datetime
# Create your models here.



class Editor(models.Model):
    name = models.CharField(max_length = 31)
    brief = models.CharField(max_length = 255, blank = True)
    fblink = models.CharField(max_length = 1023, blank= True)
    twlink = models.CharField(max_length = 1023, blank= True)

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


def content_file_name(instance, filename):
    return '/'.join(['ghoster', instance.title, filename])
class Post(models.Model):
    publish = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, allow_unicode=True)
    content = models.TextField()
    thumbnail = models.URLField(blank=True)
    cover = models.ImageField(upload_to=content_file_name, blank=True)
    editor = models.ForeignKey(Editor, default=1)
    category = models.ForeignKey(Category, default=1)
    page = models.ForeignKey(Page, default=1)
    date = models.DateTimeField(default=datetime.now)
    viewers = models.IntegerField(default=0)
    tags = TaggableManager(blank=True)


    def image_thumb(self):
        if self.cover: url = self.cover.url
        else: url = 'http://i.giphy.com/3o7ZeODTGuQOeLr3l6.gif'
        return '<img src="%(url)s" height="60" />' % {'url': url}
    image_thumb.allow_tags = True

    def short_title(self):
        return '{}'.format(self.title[:20] + ' ...')

    # @permalink
    # def get_absolute_url(self):
    #     return reverse('single_post', args={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = _('POST')
        verbose_name_plural = verbose_name
