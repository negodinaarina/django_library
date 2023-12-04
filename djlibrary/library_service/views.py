from django.shortcuts import render
from django.http import HttpResponse
import psycopg2


def index(request):
    conn = psycopg2.connect(
        database="library", user='postgres', password='1111', host='localhost', port='5433')
    conn.autocommit = True
    cursor = conn.cursor()
    if request.method == "GET":
        cursor.execute('''SELECT * FROM books JOIN authors ON books.author_id = authors.id;''')
        result = cursor.fetchall()
        data = {"data": result}
    elif request.method == "POST":
        name = request.POST.get("name", "")
        author = request.POST.get("author", "")
        cursor.execute(f'''SELECT * FROM books JOIN authors ON books.author_id = authors.id WHERE title LIKE '%{name}%' AND authors.author_name LIKE '%{author}%' ''')
        result = cursor.fetchall()
        data = {"data": result}
    return render(request, "index.html", context=data)


def about(request):
    return render(request, "about.html")


def contacts(request):
    return render(request, "contacts.html")


def places(request):
    return render(request, "places.html")


def questions(request):
    return render(request, "questions.html")

