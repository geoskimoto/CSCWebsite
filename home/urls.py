from django.urls import path, re_path
from .views import home, register

urlpatterns = [
    path('', home, name='home'),
    # path('signup/', signup, name='signup'),
    path('register/', register, name='register'),
]