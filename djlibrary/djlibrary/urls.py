from django.contrib import admin
from django.urls import path
from library_service import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about', views.about),
    path('contacts', views.contacts),
    path('places', views.places),
    path('questions', views.questions),
    path('book/<int:id>', views.book, name="book_page"),
]
