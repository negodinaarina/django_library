from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
import db.db_methods as database


def index(request):
    if request.method == "GET":
        result = database.get_all_books()
        data = {"data": result}
    elif request.method == "POST":
        name = request.POST.get("name", "")
        author = request.POST.get("author", "")
        result = database.get_books_by_params(name, author)
        data = {"data": result}
    return render(request, "index.html", context=data)


def book(request, id):
    try:
        result = database.get_book(id)
        data = {"data": result}
        return render(request, "book.html", context=data)
    except:
        return HttpResponseBadRequest("Некорректные данные")


def add_book(request):
    if request.method == "GET":
        return render(request, "add_book.html")
    elif request.method == "POST":
        data = request.POST.dict()
        if database.add_book(data):
            return redirect("/")
        else:
            return HttpResponseBadRequest("Некорректные данные")


def add_author(request):
    if request.method == "GET":
        return render(request, "add_author.html")
    elif request.method == "POST":
        data = request.POST.dict()
        if database.add_author(data):
            return redirect("/")
        else:
            return HttpResponseBadRequest("Некорректные данные")


def add_genre(request):
    if request.method == "GET":
        return render(request, "add_genre.html")
    elif request.method == "POST":
        data = request.POST.dict()
        if database.add_genre(data):
            return redirect("/")
        else:
            return HttpResponseBadRequest("Блин, что-то пошло не так")

