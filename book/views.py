from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
# from django.contrib.auth import views as auth_views

from book.models import Bunk, Room
# Create your views here.

def index(request):
    return render(request, 'book/index.html')
def bunk(request):
    return render(request, 'book/bunk.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('booking')
    else:
        form = SignUpForm()
    return render(request, 'book/signup.html', {'form': form})