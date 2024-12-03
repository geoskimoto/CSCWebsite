from django.urls import path
from .views import home, home2, about#, membership_application

urlpatterns = [
    path('', home, name='home'),
    path('home2/', home2, name='home2'),
    path('about/', about, name='about'),
]


