from .models import Author, Book, Genre


def get_book(book_id):
    book = Book.objects.get(id=book_id)
    return book


def get_author(author_name):
    author = Author.objects.get(author_name=author_name)
    return author


def get_genre(genre_name):
    genre = Genre.objects.get(genre_name=genre_name)
    return genre


def get_all_books():
    books = Book.objects.select_related('author').select_related('genre').all()
    return books


def get_books_by_params(name, author):
    books = Book.objects.select_related('author').select_related('genre')\
        .filter(title__icontains=name, author__author_name__icontains=author)
    return books


def delete_book(id): pass


def add_book(data):
    author_id = get_author(data["author"])
    genre_id = get_genre(data["genre"])
    book = Book(title=data["title"], pub_date=data["date"], description=data["descript"],
                author=author_id, genre=genre_id)
    try:
        book.save()
        return True
    except: return False


def add_author(data):
    author = Author(author_name=data["author_name"], birth_date=data["birthday"])
    try:
        author.save()
        return True
    except: return False


def add_genre(data):
    genre = Genre(genre_name=data["genre_name"])
    try:
        genre.save()
        return True
    except: return False


