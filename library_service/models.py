from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=100)
    birth_date = models.DateField()


class Genre(models.Model):
    genre_name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)



