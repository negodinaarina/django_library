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
        f'''SELECT * FROM books JOIN authors ON books.author_id = authors.id 
        JOIN genres ON books.genre_id = genres.id WHERE books.id ={id};''')
    result = cursor.fetchone()
    return result


def get_author(name):
    cursor = create_cursor()
    cursor.execute(f"SELECT id FROM authors WHERE author_name = '{name}'")
    id = cursor.fetchone()
    return id


def get_genre(name):
    cursor = create_cursor()
    cursor.execute(f"SELECT id FROM genres WHERE genre_name = '{name}';")
    id = cursor.fetchone()
    return id


def get_all_books():
    cursor = create_cursor()
    cursor.execute('''SELECT * FROM books JOIN authors ON books.author_id = authors.id;''')
    result = cursor.fetchall()
    return result


def get_books_by_params(name, author):
    cursor = create_cursor()
    cursor.execute(
        f'''SELECT * FROM books JOIN authors ON books.author_id = authors.id WHERE title 
        LIKE '%{name}%' AND authors.author_name LIKE '%{author}%' ''')
    result = cursor.fetchall()
    return result


def delete_book(id): pass


def add_book(data):
    cursor = create_cursor()
    sql = '''INSERT INTO books(title, author_id, genre_id, publication_date, description, quantity_in_stock) 
    VALUES (%s, %s, %s, %s, %s, %s)'''
    try:
        author_id = get_author(data["author"])
        genre_id = get_genre(data["genre"])
        cursor.execute(sql, (data["title"], author_id, genre_id, data["date"], data["descript"], 10))
        return True
    except:
        return False
