from django.urls import path, re_path
from .views import bunk_reservation

urlpatterns = [
    # path('', views.index, name='index'),
    path('', bunk_reservation, name='bunk_reservation'),

]