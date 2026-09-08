from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("courses/", views.courses_view, name="courses"),
    path("courses/<int:course_id>/", views.course_detail, name="course_detail"),
]