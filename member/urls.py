
from django.urls import path
from .views import CustomLoginView, dashboard, membership_registration, membership_application

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('registration/', membership_registration, name='registration'),
    path('application/', membership_application, name='membership_application'),
    path('login/', CustomLoginView.as_view(), name='login'),
]

    # path('login/', member_login_view, name="member_login"),
    # path('logout/', member_logout_view, name='member_logout'),
