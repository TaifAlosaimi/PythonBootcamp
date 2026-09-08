from django.shortcuts import render
from django.views import View

# Create your views here.


courses = [
    {
        "slug": "python",
        "title": "Python",
        "category": "Programming",
    },
    {
        "slug": "django",
        "title": "Django",
        "category": "Web Development",
    },
    {
        "slug": "html-css",
        "title": "HTML & CSS",
        "category": "Web Development",
    },
]


from django.shortcuts import render


courses = [
    {
        "slug": "python",
        "title": "Python",
        "category": "Programming",
    },
    {
        "slug": "django",
        "title": "Django",
        "category": "Web Development",
    },
    {
        "slug": "html-css",
        "title": "HTML & CSS",
        "category": "Web Development",
    },
]


def course_list(request):
    context = {
        "courses": courses
    }

    return render(request, "list.html", context)


def course_detail(request, slug):
    for course in courses:
        if course["slug"] == slug:
            context = {
                "course": course
            }

            return render(request, "detail.html", context)



def course_category(request, category):
    filtered_courses = [
        course for course in courses
        if course["category"].lower() == category.lower()
    ]

    context = {
        "courses": filtered_courses,
        "category": category
    }

    return render(request, "category.html", context)

class CourseInfoView(View):
    def get(self, request):
        return render(request, "course_info.html")


from django.http import HttpResponse

def home(request):
    print(request.method)  
    return render(request,"base.html")