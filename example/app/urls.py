from django.conf.urls import url

from .views import HomeView

urlpatterns = [
    # URLs
    url(r"^$", HomeView.as_view(), name="home"),
]
