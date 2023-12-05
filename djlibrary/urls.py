from django.contrib import admin
from django.urls import path
from library_service import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('book/<int:id>', views.book, name="book_page"),
    path('add_book', views.add_book),
    path('add_author', views.add_author),
    path('add_genre', views.add_genre),
]
