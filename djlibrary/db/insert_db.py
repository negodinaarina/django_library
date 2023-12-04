import random
import pandas as pd
import psycopg2
conn = psycopg2.connect(
   database="library", user='postgres', password='1111', host='localhost', port= '5433')
conn.autocommit = True
cursor = conn.cursor()

df = pd.read_json("books.json")
authors = list(df.author.unique())
for i in range(len(authors)):
    year = '1999-01-08'
    cursor.execute('''INSERT INTO authors(author_name, birth_date) VALUES (%s, %s)''', (authors[i], year))

genres = {1: 'fantasy', 2: 'biography', 3: 'history', 4: 'science', 5: 'romance'}
for i in range(1, 6):
    cursor.execute('''INSERT INTO genres(genre_name) VALUES (%s)''', (genres[i], ))

sql = '''INSERT INTO books(title, author_id, genre_id, publication_date, description, quantity_in_stock) VALUES (%s, %s, %s, %s, %s, %s)'''
for i in range(len(df)):
    book = df.iloc[i]
    title = book.title
    author_id = authors.index(book.author) + 1
    genre_id = random.randint(1, 5)
    publication_date = f"{abs(book.year)}-01-01"
    description = "fishtext" * 5
    quantity_in_stock = 10
    cursor.execute(sql, (title, author_id, genre_id, publication_date, description, quantity_in_stock))

