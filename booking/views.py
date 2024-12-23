from django.contrib.auth.decorators import login_required
from django.db import transaction, IntegrityError
from django.utils import timezone
from .models import Bunk, Booking
from .utils.booking_funcs import check_availability, calculate_booking_total, get_user_bookings, update_booking_dates
import datetime
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm, AvailabilityForm
from django.views.generic import ListView, FormView
from django.http import JsonResponse

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


# Need to add a check to see if there are bunk ids in the bunk table and
# if not run the "bunk_id_populater.py" script.  If the db is empty,
# current method is to just run "python book_id_populater.py"


#This function includes logic to handle concurrency issues mainting ACID db principles when booking bunks (i.e. how to
# handle issues when two members are logged in at the same time trying to book the same bunk.)
@login_required
def book_bunk(request):
    if request.method == 'POST':
        print(" POST request received.")
        form = BookingForm(request.POST)
        if form.is_valid():

            bunk = form.cleaned_data['bunk']
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']

            # Store booking details in session
            request.session['bunk'] = bunk.bunk_id
            request.session['check_in'] = check_in.isoformat()
            request.session['check_out'] = check_out.isoformat()

            try:
                with transaction.atomic():
                    # Check for conflicting bookings
                    if Booking.objects.filter(bunk=bunk.bunk_id, check_in__lt=check_out,
                                              check_out__gt=check_in).exists():
                        raise IntegrityError("This bunk is already booked for the selected time slot.")

                    # Create the booking
                    booking = Booking.objects.create(
                        user=request.user,
                        bunk=bunk,
                        check_in=check_in,
                        check_out=check_out
                    )
                    messages.success(request, f'Bunk {bunk.bunk_id} successfully booked.')
                    return redirect('dashboard')
            except IntegrityError as e:
                messages.error(request, str(e))
            except Exception as e:  # Catch unexpected errors
                messages.error(request, 'An unexpected error occurred. Please try again.')
                print(f"Unexpected error: {e}")  # Log for debugging
        else:
            messages.error(request, "Invalid form submission. Please correct the errors.")

    else:  # GET request
        form = BookingForm()


    return render(request, 'booking/book_bunk.html', {'form': form})

#using session to store booking details
# @login_required
# def book_bunk(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             bunk = form.cleaned_data['bunk']
#             check_in = form.cleaned_data['check_in']
#             check_out = form.cleaned_data['check_out']
#
#             # Store booking details in session
#             request.session['bunk'] = bunk.id
#             request.session['check_in'] = check_in.isoformat()
#             request.session['check_out'] = check_out.isoformat()
#
#             return redirect('confirm_booking')
#     else:
#         form = BookingForm()
#
#     return render(request, 'booking/book_bunk.html', {'form': form})

@login_required
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
                messages.success(request, f'Bunk {bunk.id} successfully booked.')
                return redirect('dashboard')
        except IntegrityError:
            messages.error(request, 'The selected bunk is already booked for the given time period. Please choose a different time or bunk.')

    return render(request, 'booking/confirm_booking.html', {
        'bunk': bunk,
        'check_in': check_in,
        'check_out': check_out,
    })


class BunkList(ListView):
    model=Bunk


class BookingList(ListView):
    model=Booking



#https://www.youtube.com/watch?v=m7uVhLxT1AA&list=PL_6Ho1hjJirn8WbY4xfVUAlcn51E4cSbY&index=2
# at 17:45min.
# class BookingView(FormView):
#     form_class = AvailabilityForm
#     template_name='availability_form.html'
#     def form_valid(self, form):
#         data = form.cleaned_data
#         bunk_list = Bunk
#         available_bunks = []
#         for bunk in get_all_bunks():
#             if check_availability(bunk, data['check_in'], data['check_out']):
#                 available_bunks.append(bunk)
#         # Handle this differently later.  Just selecting the first available bunk and booking it.:
#         if len(available_bunks)>0: # making sure everything is not booked.
#             bunk_to_book = available_bunks[0]
#             booking = Booking.objects.create(
#                 user=request.user,
#                 bunk=bunk_to_book,
#                 check_in=data['check_in'],
#                 check_out=data['check_out']
#             )
#             booking.save()
#             return HttpResponse(booking)
#         else:
#             HttpResponse('Bunks are fully booked.')
@login_required
def initiate_payment(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking_total = calculate_booking_total(booking)

    intent = stripe.PaymentIntent.create(
        amount=int(booking_total * 100), # amount in cents
        currency='usd',
        description=f'Booking payment for {booking.bunk_id}',
        metadata={'booking_id':booking.bunk_id}
    )
    return render(request,
                  'payment_form.html',
                  {'client_secret': intent.client_secret}
                  )

@login_required
def handle_payment_confirmation(request):
    # Handle Stripe webhook or redirect to a success page after payment confirmation.
    # Eventually, send an email confirmation of the booking plus a payment confirmation page.
    return render(request, 'payment_success.html')


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
