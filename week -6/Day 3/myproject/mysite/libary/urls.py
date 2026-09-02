from django.urls import path
from .views import book_list, book_detail

urlpatterns = [
    path("", book_list, name="book_list"),
    path("books/", book_list, name="book_list"),
    path("books/<int:id>/", book_detail, name="book_detail"),
]