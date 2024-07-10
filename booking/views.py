from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# from .forms import BunkReservationForm
from django.db import transaction, IntegrityError
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Bunk, Booking
from .forms import BookingForm
from django.contrib import messages
import datetime

#This function includes logic to handle concurrency issues mainting ACID db principles when booking bunks (i.e. how to
# handle issues when two members are logged in at the same time trying to book the same bunk.)
# @login_required
# def book_bunk(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             bunk = form.cleaned_data['bunk']
#             check_in = form.cleaned_data['check_in']
#             check_out = form.cleaned_data['check_out']
#
#             try:
#                 with transaction.atomic():
#                     if Booking.objects.filter(bunk=bunk.bunk_number, check_in__lt=check_out, check_out__gt=check_in).exists():
#                         raise IntegrityError("This room is already booked for the selected time slot.")
#
#                     booking = Booking.objects.create(
#                         user=request.user,
#                         bunk=bunk,
#                         check_in=check_in,
#                         check_out=check_out
#                     )
#                     messages.success(request, f'Bunk {bunk.bunk_number} successfully booked.')
#                     return redirect('dashboard')
#             except IntegrityError:
#                 messages.error(request,
#                                'The selected room is already booked for the given time period. Please choose a different time or room.')
#     else:
#         form = BookingForm()
#
#     return render(request, 'booking/book_bunk.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm
from .models import Booking, Bunk

#using session to store booking details
@login_required
def book_bunk(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            bunk = form.cleaned_data['bunk']
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']

            # Store booking details in session
            request.session['bunk'] = bunk.id
            request.session['check_in'] = check_in.isoformat()
            request.session['check_out'] = check_out.isoformat()

            return redirect('confirm_booking')
    else:
        form = BookingForm()

    return render(request, 'booking/book_bunk.html', {'form': form})

def confirm_booking(request):
    # Retrieve booking details from session
    bunk_id = request.session.get('bunk')
    check_in = request.session.get('check_in')
    check_out = request.session.get('check_out')

    if not all([bunk_id, check_in, check_out]):
        messages.error(request, 'Incomplete booking details.')
        return redirect('book_bunk')

    bunk = Bunk.objects.get(id=bunk_id)
    check_in = datetime.fromisoformat(check_in)
    check_out = datetime.fromisoformat(check_out)

    if request.method == 'POST':
        try:
            with transaction.atomic():
                if Booking.objects.filter(bunk=bunk, check_in__lt=check_out, check_out__gt=check_in).exists():
                    raise IntegrityError("This bunk is already booked for the selected time slot.")

                Booking.objects.create(
                    user=request.user,
                    bunk=bunk,
                    check_in=check_in,
                    check_out=check_out
                )
                messages.success(request, f'Bunk {bunk.bunk_number} successfully booked.')
                return redirect('dashboard')
        except IntegrityError:
            messages.error(request, 'The selected bunk is already booked for the given time period. Please choose a different time or bunk.')

    return render(request, 'booking/confirm_booking.html', {
        'bunk': bunk,
        'check_in': check_in,
        'check_out': check_out,
    })

# @login_required
# def bunk_reservation(request):
#     if request.method == 'POST':
#         form = BunkReservationForm(request.POST)
#         if form.is_valid():
#             # Process form data
#             # Save reservation, etc.
#             return redirect('reservation_success')  # Redirect to a success page
#     else:
#         #NEED TO DO SOMETHING HERE...REDIRECT TO LOGIN SCREEN
#         form = BunkReservationForm()
#         # return redirect("need to login")
#     context = {
#         'form': form,
#     }
#     return render(request, 'bunk_reservation.html')
