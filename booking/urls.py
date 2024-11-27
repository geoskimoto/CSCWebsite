from django.urls import path, include
from .views import book_bunk


urlpatterns = [
    path('/booking', book_bunk, name="book_bunk")
    ]