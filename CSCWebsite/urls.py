"""CSCWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from member import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    # path('login/', auth_views.LoginView.as_view(template_name='member/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='member/logout.html'), name='logout'),
    # path('signup/', views.signup, name='signup'),
    # path('register/', views.register, name='register'),
    path('booking/', include('booking.urls'), name='booking'),
    path('member/', include('member.urls'), name='member'),
    path('', include('home.urls'), name='home'),
    # path('bunks/', include('member.urls'))
    # path('', include('HomePage.urls')),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

