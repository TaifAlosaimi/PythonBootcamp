from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="list"),
    path("<int:id>/", views.post_detail, name="detail"),
    path("category/<slug:name>/", views.category, name="category"),
]