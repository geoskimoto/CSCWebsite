from django.contrib import admin

from .models import Bunk, Booking, Billing, Payment
# Register your models here.

admin.site.register(Bunk)
admin.site.register(Booking)
admin.site.register(Billing)
admin.site.register(Payment)