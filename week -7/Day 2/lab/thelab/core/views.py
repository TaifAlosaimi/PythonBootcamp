from django.shortcuts import render


courses = [
    {
        "id": 1,
        "name": "Astronomy",
        "level": "Beginner",
        "students": 24,
        "description": "<strong>Explore the universe</strong> through stars, galaxies, planets, and modern astronomy.",
        "image": "astronomy.jpg",
    },
    {
        "id": 2,
        "name": "Astrophysics",
        "level": "Intermediate",
        "students": 18,
        "description": "Learn how physics helps us understand stars and black holes.",
        "image": "astrophysics.jpg",
    },
    {
        "id": 3,
        "name": "Planetary Science",
        "level": "Advanced",
        "students": 0,
        "description": "Study planets, moons, atmospheres, and worlds beyond Earth.",
        "image": "planetary-science.jpg",
    },
]


def home(request):
    context = {
        "username": "Taif",
        "courses": courses,
    }

    return render(request, "core/home.html", context)


def courses_view(request):
    context = {
        "username": "Taif",
        "courses": courses,
    }

    return render(request, "core/courses.html", context)


def course_detail(request, course_id):
    course = None

    for item in courses:
        if item["id"] == course_id:
            course = item
            break

    context = {
        "course": course,
    }

    return render(request, "core/course_detail.html", context)