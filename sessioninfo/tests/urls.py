"""URLs to run the tests."""
from django.conf.urls import patterns, include, url
from django.contrib import admin

from sessioninfo.tests.test_app.views import get_session_user_view

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^get-session-user/', get_session_user_view),
)