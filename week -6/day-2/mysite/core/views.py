from django.shortcuts import render
from django.http import HttpResponse 
def home(requests):
    return HttpResponse("Welcome To Home Page")
def about(requests):
    return HttpResponse("Welcome To About Page")
def contact(requests):
    return HttpResponse("Welcome To Contact Page")

# Create your views here.
