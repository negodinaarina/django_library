import psycopg2
import os
conn = psycopg2.connect(
   database=f"{os.environ.get('POSTGRES_NAME')}", user=f"{os.environ.get('POSTGRES_USER')}",
   password=f"{os.environ.get('POSTGRES_PASSWORD')}", host='db', port='5432')
conn.autocommit = True

cursor = conn.cursor()


sql = '''CREATE TABLE IF NOT EXISTS authors
(
    id SERIAL PRIMARY KEY,
    author_name CHAR(55) NOT NULL, 
    birth_date DATE NOT NULL
);'''
cursor.execute(sql)
conn.commit()
print("Created books authors........")

sql = '''CREATE TABLE IF NOT EXISTS genres
(
    id SERIAL PRIMARY KEY,
    genre_name CHAR(55) NOT NULL
);'''
cursor.execute(sql)
conn.commit()
print("Created books genres........")

sql = '''CREATE TABLE IF NOT EXISTS books
(
    id SERIAL PRIMARY KEY,
    title CHAR(55) NOT NULL,
    author_id INTEGER NOT NULL REFERENCES authors (id),
    genre_id INTEGER NOT NULL REFERENCES genres (id),
    publication_date DATE NOT NULL,
    description TEXT NOT NULL, 
    quantity_in_stock INTEGER
);'''
cursor.execute(sql)
conn.commit()
print("Created books table........")
conn.close()