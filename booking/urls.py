from django.urls import path, include
from .views import book_bunk


urlpatterns = [
    path('book_bunk/', book_bunk, name="book_bunk")
    ]