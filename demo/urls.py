from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from .views import HomeView

urlpatterns = patterns(
    # Prefix
    '',

    # URLs
    url(r'^$', HomeView.as_view(), name='home'),
)
