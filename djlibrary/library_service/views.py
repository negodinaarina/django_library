from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
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


# def edit_book(request, id):
#     try:
#         conn = psycopg2.connect(
#             database="library", user='postgres', password='1111', host='localhost', port='5433')
#         conn.autocommit = True
#         cursor = conn.cursor()
#         cursor.execute(f'''SELECT * FROM books JOIN authors ON books.author_id = authors.id JOIN genres ON books.genre_id = genres.id WHERE books.id ={id};''')
#         result = cursor.fetchone()
#         data = {"data": result}
#         return render(request, "edit.html", context=data)
#     except:
#         return HttpResponseBadRequest("Некорректные данные")
#
#
# def delete_book(request, id):
#     try:
#         conn = psycopg2.connect(
#             database="library", user='postgres', password='1111', host='localhost', port='5433')
#         conn.autocommit = True
#         cursor = conn.cursor()
#         cursor.execute(f'''DELETE FROM books WHERE books.id ={id};''')
#         conn.commit()
#         return render(request, "index.html")
#     except:
#         return HttpResponseBadRequest("Некорректные данные")

