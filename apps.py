from django.apps import AppConfig
from django.conf import settings

class GhosterConfig(AppConfig):
    name = 'ghoster'
    verbose_name = "GHOSTER CMS"
    settings.TEMPLATES[0]['OPTIONS']['context_processors'].append('ghoster.context_processors.application')

