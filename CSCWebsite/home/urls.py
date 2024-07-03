from django.urls import path
from .views import home, about#, membership_application

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    # path('signup/', signup_view, name='signup'),
    # path('register/', register, name='register'),
    # path('application/', membership_application, name='membership_application'),
]


