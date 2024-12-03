from django.contrib import admin
<<<<<<< HEAD
=======
from .models import Member, MemberApplication, FamilyMember, Locker #, Reservation, Payment, Bunk
>>>>>>> origin/laptop
from .models import Member, FamilyMember, Locker #, Reservation, Payment, Bunk
# Register your models here.

admin.site.register(Member)
admin.site.register(MemberApplication)
admin.site.register(FamilyMember)
admin.site.register(Locker)
# admin.site.register(Bunk)
# admin.site.register(Reservation)
# admin.site.register(Payment)


# @admin.register(Member)
# class MemberAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'date_joined', 'last_login', 'is_active', 'is_staff')
#     search_fields = ('email', 'username')
#     readonly_fields = ('date_joined', 'last_login')
#
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()