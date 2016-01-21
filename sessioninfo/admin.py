# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session


class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    _session_data.short_description = 'Session Data'

    def username(self, obj):
        uid = self._session_data(obj).get('_auth_user_id')
        return User.objects.get(pk=uid)

    def user_id(self, obj):
        return self._session_data(obj).get('_auth_user_id')

    def user_hash(self, obj):
        return self._session_data(obj).get('_auth_user_hash')

    def auth_backend(self, obj):
        return self._session_data(obj).get('_auth_user_backend')

    readonly_fields = ['_session_data', 'username', 'user_id', 'user_hash',
                       'auth_backend']
    fieldsets = (
        ('Session Information', {
            'fields': ('session_key', '_session_data', 'expire_date')}),
        ('Auth Information', {
            'fields': ('username', 'user_id', 'user_hash', 'auth_backend')}),
    )
    list_display = ['username', 'auth_backend', 'session_key', '_session_data',
                    'expire_date']
    ordering = ['-expire_date']


show_sessions = getattr(settings, 'SHOW_SESSIONS_IN_ADMIN', False)
if show_sessions:
    admin.site.register(Session, SessionAdmin)
