# -*- coding: utf-8 -*-

try:
    from django.apps import AppConfig
except ImportError:
    pass  # Django < 1.7
else:

    class Config(AppConfig):
        name = 'sessioninfo'
        verbose_name = ''