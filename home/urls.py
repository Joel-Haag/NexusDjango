from django.urls import path
from . import views


app_name = "home"


urlpatterns = [
    path("", views.HomeView, name="HomeView"),
    path("", views.contact, name="contact"),
]
