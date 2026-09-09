from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

COURSES = [
    {
        "id": 1,
        "title": "Python Fundamentals",
        "category": "Programming",
        "difficulty": "Beginner",
        "description": "Learn Python basics, variables, conditions, loops, and functions.",
        "instructor": "Sarah Ahmed",
        "duration": "4 weeks",
    },
    {
        "id": 2,
        "title": "Django Web Development",
        "category": "Web Development",
        "difficulty": "Intermediate",
        "description": "Build dynamic web applications using Django and Python.",
        "instructor": "Omar Ali",
        "duration": "6 weeks",
    },
    {
        "id": 3,
        "title": "HTML & CSS Essentials",
        "category": "Web Development",
        "difficulty": "Beginner",
        "description": "Learn how to structure and style modern web pages.",
        "instructor": "Lina Hassan",
        "duration": "3 weeks",
    },
    {
        "id": 4,
        "title": "Advanced Python",
        "category": "Programming",
        "difficulty": "Advanced",
        "description": "Explore advanced Python concepts and object-oriented programming.",
        "instructor": "Khalid Saad",
        "duration": "5 weeks",
    },
    {
        "id": 5,
        "title": "Database Fundamentals",
        "category": "Database",
        "difficulty": "Intermediate",
        "description": "Understand databases, SQL queries, and data relationships.",
        "instructor": "Nora Faisal",
        "duration": "4 weeks",
    },
    {
        "id": 6,
        "title": "JavaScript Basics",
        "category": "Programming",
        "difficulty": "Beginner",
        "description": "Learn JavaScript fundamentals and interactive web behavior.",
        "instructor": "Maha Abdullah",
        "duration": "4 weeks",
    },
]


def course_list(request):
    q = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    difficulty = request.GET.get("difficulty", "").strip()

    filtered_courses = COURSES

    if q:
        filtered_courses = [
            course
            for course in filtered_courses
            if q.lower() in course["title"].lower()
            or q.lower() in course["description"].lower()
        ]

    if category:
        filtered_courses = [
            course
            for course in filtered_courses
            if course["category"] == category
        ]

    if difficulty:
        filtered_courses = [
            course
            for course in filtered_courses
            if course["difficulty"] == difficulty
        ]

    paginator = Paginator(filtered_courses, 3)

    page_number = request.GET.get("page", "1")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "q": q,
        "category": category,
        "difficulty": difficulty,
    }

    return render(request, "courses/course_list.html", context)


def course_detail(request, id):
    course = next(
        (course for course in COURSES if course["id"] == id),
        None
    )

    if course is None:
        return HttpResponse("Course not found", status=404)

    tab = request.GET.get("tab", "details")

    allowed_tabs = {"details", "syllabus", "instructor"}

    if tab not in allowed_tabs:
        tab = "details"

    context = {
        "course": course,
        "tab": tab,
    }

    return render(request, "courses/course_detail.html", context)