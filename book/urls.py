from django.urls import path, re_path
from book import views

urlpatterns= [
    re_path(r'^$', views.index, name='index'),
    path('bunk/', views.bunk, name='bunk')
]