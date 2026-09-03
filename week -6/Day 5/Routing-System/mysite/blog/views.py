from django.shortcuts import render

# Create your views here.



def post_list(request):
    return render(request, "list.html")


def post_detail(request, id):
    return render(request, "detail.html")


def category(request, name):
    return render(request, "category.html")