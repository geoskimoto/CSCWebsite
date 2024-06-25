from django.db import models

class Bunk(models.Model):
    bunk_number = models.CharField(max_length=10, unique=True)
    assigned_to = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True, related_name='bunks')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, default=20.00)
    area = models.CharField(max_length=50)  # e.g., North Wing, South Wing

class Reservation(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='reservations')
    bunk = models.ForeignKey(Bunk, on_delete=models.CASCADE, related_name='reservations')
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

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
    reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')
    locker = models.ForeignKey(Locker, on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')

# class Member(AbstractBaseUser):
#     name = models.CharField(max_length=100, default=None)
#     username = models.CharField(max_length=100, default=None)
#     email = models.EmailField(unique=True, default=None)
#     status = models.CharField(max_length=25, default="Primary Member")
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(null=True, blank=True)
#     emergency_contact = models.CharField(max_length=100, default=None)
#     emergency_contact_phone = models.BigIntegerField(default=None)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#
#     objects = MemberManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name', 'username', 'status', 'emergency_contact', 'emergency_contact_phone']
#
#     def __str__(self):
#         return self.email
#
# class Bunk(models.Model):
#     area = models.CharField(max_length=100)
#     bunk_number = models.BigIntegerField(unique=True)
#     reservation = models.CharField(max_length=100)  #need to make this a foreign key and have it reference a table with all members.
#
# class Room(models.Model):
#     room = models.CharField(max_length=100)
#