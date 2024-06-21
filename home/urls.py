from django.urls import path
from .views import home, about, membership_application, login

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('about/', about, name='about'),
    # path('signup/', signup_view, name='signup'),
    # path('register/', register, name='register'),
    path('membership-application/', membership_application, name='membership_application'),
]

