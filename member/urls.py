from django.urls import path, re_path
from .views import bunk

urlpatterns = [
    # path('', views.index, name='index'),
    path('', bunk, name='bunk'),

]