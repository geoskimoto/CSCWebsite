from ..models import Booking, Bunk
from django.shortcuts import render, redirect
# import stripe



# From https://www.youtube.com/watch?v=-9dhCQ7FdD0&list=PL_6Ho1hjJirn8WbY4xfVUAlcn51E4cSbY at around 29mins.
def check_availability(bunk, check_in, check_out):
    avail_list = []
    booking_list = Booking.objects.filter(bunk=bunk)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)

def calculate_booking_total(self):
    room_price_per_night = self.bunk #.room_type.roomtype_price
    check_in = self.check_in
    check_out = self.check_out
    # Calculate duration of stay in nights
    duration = (check_out - check_in).days
    # Calculate total room price based on duration
    total_price = room_price_per_night * duration
    # services_price = sum(service.service_price for service in self.services.all())
    total_amount = total_price #+ services_price

    return total_amount


def get_user_bookings(user):
    return Booking.objects.filter(user=user)

def get_all_bunks():
    bunks=Bunk.objects.values_list('bunk_numbers', flat=True)
    return list(bunks)
def update_booking_dates(booking_id, new_check_in, new_check_out):
    try:
        booking = Booking.objects.get(id=booking_id)
        booking.check_in = new_check_in
        booking.check_out = new_check_out
        booking.save()
        return True
    except Booking.DoesNotExist:
        return False

