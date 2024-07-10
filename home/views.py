from django.urls import path, re_path
# from .views import home, about, register, signup_view, login
from django.shortcuts import render, redirect
# from .forms import MembershipApplicationForm
#
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login, authenticate
# from member.forms import SignUpForm
# from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
# Create your views here.



def home(request):
    return render(request, 'home/home.html')

def home2(request):
    return render(request, 'home/home2.html')
def about(request):
    return render(request, 'home/about.html')

# def membership_application(request):
#     if request.method == 'POST':
#         form = MembershipApplicationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success_url')  # Redirect to a success page
#     else:
#         form = MembershipApplicationForm()
#     return render(request, 'home/membership_application.html', {'form': form})


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(email=email, password=raw_password)
#             login(request, user)
#             return redirect('booking')
#     else:
#         form = SignUpForm()
#     return render(request, 'member/signup.html', {'form': form})

# def signup_view(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Redirect to a success page or login page
#             return redirect('login')  # Replace with your desired URL name for login
#     else:
#         form = SignUpForm()
#     return render(request, 'member/signup.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirect to login page after successful registration
#     else:
#         form = UserCreationForm()
#     return render(request, 'member/register.html', {'form': form})