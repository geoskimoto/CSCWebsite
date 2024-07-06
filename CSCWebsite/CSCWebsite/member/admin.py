from django.contrib import admin
<<<<<<< HEAD:member/admin.py
from .models import Member, MemberApplication, FamilyMember, Locker #, Reservation, Payment, Bunk
=======
from .models import Member, FamilyMember, Locker #, Reservation, Payment, Bunk
>>>>>>> e7f7f3140afd1e3098b5c6ad0e0ab9f899b2cad4:CSCWebsite/member/admin.py
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