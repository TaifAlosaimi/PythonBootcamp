


from django.shortcuts import render

def home(request):
    courses = ["Space System Engineering", "Data analysit", "Python"]

    context = {
        "name": "Taif",
        "course": "Python Web Development",
        "courses": courses
    }

    return render(request, "ta/home.html", context)


def about(request):
    return render(request, "ta/about.html")


def contact(request):
    return render(request, "ta/contact.html")