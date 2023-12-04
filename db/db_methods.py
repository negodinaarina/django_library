import psycopg2


def create_cursor():
    conn = psycopg2.connect(
        database="library", user='postgres', password='1111', host='localhost', port='5433')
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor


def get_book(id):
    cursor = create_cursor()
    cursor.execute(
        f'''SELECT * FROM books JOIN authors ON books.author_id = authors.id JOIN genres ON books.genre_id = genres.id WHERE books.id ={id};''')
    result = cursor.fetchone()
    return result


def get_all_books():
    cursor = create_cursor()
    cursor.execute('''SELECT * FROM books JOIN authors ON books.author_id = authors.id;''')
    result = cursor.fetchall()
    return result


def get_books_by_params(name, author):
    cursor = create_cursor()
    cursor.execute(
        f'''SELECT * FROM books JOIN authors ON books.author_id = authors.id WHERE title LIKE '%{name}%' AND authors.author_name LIKE '%{author}%' ''')
    result = cursor.fetchall()
    return result