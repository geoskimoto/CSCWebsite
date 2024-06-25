from django.urls import path
from .views import home, about, membership_application, login2

urlpatterns = [
    path('', home, name='home'),
    path('login2/', login2, name='login'),
    path('about/', about, name='about'),
    # path('signup/', signup_view, name='signup'),
    # path('register/', register, name='register'),
    path('membership-application/', membership_application, name='membership_application'),
]


