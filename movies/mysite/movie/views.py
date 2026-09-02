from django.shortcuts import render

# Create your views here.

movies = [
    {"id": 1, "title": "Interstellar", "year": 2014, "rating": 8.7},
    {"id": 2, "title": "Inception", "year": 2010, "rating": 8.8},
    {"id": 3, "title": "The Dark Knight", "year": 2008, "rating": 9.0},
]

def movie_list(request):
    context = {
        "movies": movies
    }

    return render(request, "movie/list_movie.html", context)

def movie_detail(request, id):
    movie=None
    for movie in movies:
        if movie["id"] == id:
            context = {
                "movie": movie
            }
    return render(request, "movie/detail.html", context)