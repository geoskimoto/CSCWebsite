from django.db import models
from django.conf import settings

#going to say unresolved reference because booking app above member app, so IDE think it doesn't exist yet.  Django
#ORM will handle it though.
from member.models import Member

# From https://www.youtube.com/watch?v=-9dhCQ7FdD0&list=PL_6Ho1hjJirn8WbY4xfVUAlcn51E4cSbY
# class Room(models.Model):
#     ROOM_OPTIONS = (
#         ('Bunk'),
#         ('Room A'),
#         ('Room B')
#     )
#     number = models.IntegerField()
#     option = models.CharField(max_length=10, choices=ROOM_OPTIONS)

# ------------------

class Bunk(models.Model):
    bunk_number = models.CharField(max_length=10, unique=True)
    assigned_to = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True, related_name='bunks')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, default=20.00)
    area = models.CharField(max_length=50)
    sub_area = models.CharField(max_length=50, null=True)

    #This is important, or else you'll just have "Bunk Object (1)" as the name for each bunk in the forms and admin interface.
    def __str__(self):
        return self.bunk_number
class Booking(models.Model):
    booking_id = models.CharField(max_length=50, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bunk = models.ForeignKey(Bunk, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('bunk', 'check_in', 'check_out')

    # def calculate_total(self):
    #     room_price_per_night = self.bunk #.room_type.roomtype_price
    #     check_in = self.check_in
    #     check_out = self.check_out
    #     # Calculate duration of stay in nights
    #     duration = (check_out - check_in).days
    #     # Calculate total room price based on duration
    #     total_price = room_price_per_night * duration
    #     # services_price = sum(service.service_price for service in self.services.all())
    #     total_amount = total_price #+ services_price
    #
    #     return total_amount


class Billing(models.Model):
    member = models.ForeignKey(Member, related_name='billing_invoices', on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    due_date = models.DateField()

    def __str__(self):
        return f'Billing {self.id} for {self.member}'


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

