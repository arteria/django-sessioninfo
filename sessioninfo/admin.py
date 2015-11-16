# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin
from django.contrib.sessions.models import Session


class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()

    list_display = ['session_key', '_session_data', 'expire_date']


show_sessions = getattr(settings, 'SHOW_SESSIONS_IN_ADMIN', False)
if show_sessions:
    admin.site.register(Session, SessionAdmin)
