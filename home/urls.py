from django.urls import path, re_path
from .views import home, about, register, signup_view

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('signup/', signup_view, name='signup'),
    path('register/', register, name='register'),
]