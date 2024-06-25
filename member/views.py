from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from .forms import SignUpForm
# from django.contrib.auth import views as auth_views
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Currently if you're not logged in already, this will just go to a broken page.
# Don't be fooled, it's working, just need to handle what happens when you're not logged in (ie. create a redirect login html file)
# @login_required
# def bunk(request):
#     return render(request, 'member/bunk.html')

@login_required
def member_base(request):
    return render(request, 'member_base.html')

