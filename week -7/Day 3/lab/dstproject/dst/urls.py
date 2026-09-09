from django.urls import path

from . import views


app_name = "dst"


urlpatterns = [
    path("", views.upload, name="upload"),
]