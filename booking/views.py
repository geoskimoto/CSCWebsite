from django.shortcuts import render
from .forms import BunkReservationForm
from django.db import transaction, IntegrityError
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Room, Booking
from .forms import BookingForm
from django.contrib import messages


#This function includes logic to handle concurrency issues mainting ACID db principles when booking bunks (i.e. how to
# handle issues when two members are logged in at the same time trying to book the same bunk.)
@login_required
def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            room = form.cleaned_data['room']
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']

            try:
                with transaction.atomic():
                    if Booking.objects.filter(room=room, check_in__lt=check_out, check_out__gt=check_in).exists():
                        raise IntegrityError("This room is already booked for the selected time slot.")

                    booking = Booking.objects.create(
                        user=request.user,
                        room=room,
                        check_in=check_in,
                        check_out=check_out
                    )
                    messages.success(request, f'Room {room.name} successfully booked.')
                    return redirect('dashboard')
            except IntegrityError:
                messages.error(request,
                               'The selected room is already booked for the given time period. Please choose a different time or room.')
    else:
        form = BookingForm()

    return render(request, 'booking/book_room.html', {'form': form})



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
