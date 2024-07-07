from django.db import models
#going to say unresolved reference because booking app above member app, so IDE think it doesn't exist yet.  Django
#ORM will handle it though.
from member.models import Member
class Bunk(models.Model):
    bunk_number = models.CharField(max_length=10, unique=True)
    assigned_to = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True, related_name='bunks')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, default=20.00)
    area = models.CharField(max_length=50)  # e.g., North Wing, South Wing

class Booking(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='reservations')
    bunk = models.ForeignKey(Bunk, on_delete=models.CASCADE, related_name='reservations')
    # services = models.ManyToManyField('Service')  # Include services booked
    booking_date = models.DateField(auto_now_add=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_total(self):
        room_price_per_night = self.room.room_type.roomtype_price
        check_in = self.check_in_date
        check_out = self.check_out_date
        # Calculate duration of stay in nights
        duration = (check_out - check_in).days
        # Calculate total room price based on duration
        total_room_price = room_price_per_night * duration
        services_price = sum(service.service_price for service in self.services.all())
        total_amount = total_room_price + services_price

        return total_amount

class Billing(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='invoices')
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.total_amount = self.booking.total_price
        super().save(*args, **kwargs)
class Payment(models.Model):
    PAYMENT_METHODS = [
        ('CC', 'Credit Card'),
        ('PP', 'PayPal'),
        # Add other payment methods as necessary
    ]
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=2, choices=PAYMENT_METHODS)
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update member's balance after saving payment
        self.member.update_balance()

class Invoice(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='invoices')
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='invoices')
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    issued_date = models.DateField(auto_now_add=True)
    paid_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.amount_due = self.booking.total_price
        super().save(*args, **kwargs)
        self.member.update_balance()
