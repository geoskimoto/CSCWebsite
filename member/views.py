from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import EmailAuthenticationForm


@login_required
def dashboard(request):
    # This view requires the user to be logged in
    return render(request, 'member/dashboard.html')


def member_login_view(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('member/dashboard')  # Redirect to dashboard upon successful login
        else:
            messages.error(request, 'Invalid email or password.')
    else:
        form = EmailAuthenticationForm()

    return render(request, 'member/login.html', {'form': form})

def member_logout_view(request):
    logout(request)
    # Redirect to the login page or any other page after logout
    return redirect('member/login')

# def member_login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 # Redirect to a success page
#                 return redirect('dashboard')  # Replace 'dashboard' with your desired URL name
#             else:
#                 messages.error(request, 'Invalid username or password.')
#         else:
#             messages.error(request, 'Invalid username or password.')
#     else:
#         form = AuthenticationForm()
#
#     return render(request, 'member/login.html', {'form': form})
def booking_view(request):
    # Retrieve room types from the database
    # room_types = RoomType.objects.all()  # Fetch all room types (this could be more specific as needed)
    # Pass room types data to the template as context
    return render(request, 'booking.html') #, {'room_types': room_types})





def incorrectDetails(request):
    return render(request, "incorrectDetails.html")


def forgetPassword(request):
    return render(request, "password_reset.html")
