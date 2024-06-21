from django.urls import path, re_path
from .views import bunk_reservation, member_base

urlpatterns = [
    path('', member_base, name='member_base'),
    path('reservations/', bunk_reservation, name='bunk_reservation'),
]