from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap

app_name = "home"

sitemaps = {"static": StaticSitemap}  # add StaticSitemap to the dictionary


urlpatterns = [
    path("", views.HomeView.as_view(), name=""),
    path("", views.contact, name="contact"),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
