from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from .forms import SignUpForm
# from django.contrib.auth import views as auth_views
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import BunkReservationForm

# Create your views here.

# Currently if you're not logged in already, this will just go to a broken page.
# Don't be fooled, it's working, just need to handle what happens when you're not logged in (ie. create a redirect login html file)
# @login_required
# def bunk(request):
#     return render(request, 'member/bunk.html')

@login_required
def member_base(request):
    return render(request, 'member_base.html')

@login_required
def bunk_reservation(request):
    if request.method == 'POST':
        form = BunkReservationForm(request.POST)
        if form.is_valid():
            # Process form data
            # Save reservation, etc.
            return redirect('reservation_success')  # Redirect to a success page
    else:
        #NEED TO DO SOMETHING HERE...REDIRECT TO LOGIN SCREEN
        form = BunkReservationForm()
        # return redirect("need to login")
    context = {
        'form': form,
    }
    return render(request, 'bunk_reservation.html')