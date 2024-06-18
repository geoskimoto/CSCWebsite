from django.urls import path, re_path
from .views import register, bunk, signup, register

urlpatterns = [
    # path('', views.index, name='index'),
    path('bunk/', bunk, name='bunk'),
    path('signup/', signup, name='signup'),
    path('register/', register, name='register'),
]