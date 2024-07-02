from django.urls import path, re_path
from .views import member_login_view, member_logout_view, dashboard, membership_registration

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('/registration', membership_registration, name='registration')
    # path('login/', member_login_view, name="member_login"),
    # path('logout/', member_logout_view, name='member_logout'),
]