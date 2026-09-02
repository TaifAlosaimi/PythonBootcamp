from django.shortcuts import render

# Create your views here.
books = [
    {"id": 1, "title": "Welcome to Django", "author": "Abdullah Albassami", "year": 2026},
    {"id": 2, "title": "FastAPI demystified", "author": "Taif Alosaimi", "year": 2026},
]

def book_list(request):
    context = {
        "books": books
    }

    return render(request, "library/list.html", context)

def book_detail(request, id):
    for book in books:
        if book["id"] == id:
            context = {"book": book}
            return render(request, "library/detail.html", context)