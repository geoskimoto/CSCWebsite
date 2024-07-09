from django.urls import path
from .views import home, about#, membership_application

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),

]


