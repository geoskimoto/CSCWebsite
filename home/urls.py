from django.urls import path
<<<<<<< HEAD
from .views import home, about, membership_application

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    # path('signup/', signup_view, name='signup'),
    # path('register/', register, name='register'),
    path('application/', membership_application, name='membership_application'),
=======
from .views import home, home2, about#, membership_application

urlpatterns = [
    path('', home, name='home'),
    path('home2/', home2, name='home2'),
    path('about/', about, name='about'),

>>>>>>> origin/laptop
]


