from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import EmailAuthenticationForm, MembershipRegistrationForm, MembershipApplicationForm

from django.conf import settings
User = settings.AUTH_USER_MODEL

from django.shortcuts import render, redirect
from .forms import UserCreationWithEmailForm, MembershipRegistrationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy


def membership_registration(request):
    if request.method == 'POST':
        user_form = UserCreationWithEmailForm(request.POST)
        member_form = MembershipRegistrationForm(request.POST)
        if user_form.is_valid() and member_form.is_valid():
            user = user_form.save()
            member = member_form.save(commit=False)
            member.user = user  # Assuming Member has a ForeignKey to User
            member.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        user_form = UserCreationWithEmailForm()
        member_form = MembershipRegistrationForm()

    return render(request, 'member/membership_registration.html', {
        'user_form': user_form,
        'member_form': member_form,
    })


def membership_application(request):
    if request.method == 'POST':
        form = MembershipApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success page
    else:
        form = MembershipApplicationForm()
    return render(request, 'member/membership_application.html', {'form': form})

# def membership_registration(request):
#     if request.method == 'POST':
#         form = MembershipRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success_url')  # Redirect to a success page
#     else:
#         form = MembershipRegistrationForm()
#     return render(request, 'member/membership_registration.html', {'form': form})



@login_required
def dashboard(request):
    return render(request, 'member/dashboard.html')



class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('dashboard'))  # Ensure this uses reverse_lazy to get the correct absolute URL
        return super().dispatch(request, *args, **kwargs)


def member_login_view(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard upon successful login
        else:
            messages.error(request, 'Invalid email or password.')
    else:
        form = EmailAuthenticationForm()

    return render(request, 'member/login.html', {'form': form})

def member_logout_view(request):
    logout(request)
    # Redirect to the login page or any other page after logout
    return redirect('login')

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