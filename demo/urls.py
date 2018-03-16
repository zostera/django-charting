from __future__ import unicode_literals

from django.conf.urls import include, url

from .views import HomeView

urlpatterns = [
    # URLs
    url(r'^$', HomeView.as_view(), name='home'),
]
