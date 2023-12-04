from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contacts(request):
    return render(request, "contacts.html")


def places(request):
    return render(request, "places.html")


def questions(request):
    return render(request, "questions.html")