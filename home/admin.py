from django.contrib import admin
from .models import Bunk, Member
# Register your models here.

admin.site.register(Bunk)
# admin.site.register(Room)
admin.site.register(Member)


# @admin.register(Member)
# class MemberAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'date_joined', 'last_login', 'is_active', 'is_staff')
#     search_fields = ('email', 'username')
#     readonly_fields = ('date_joined', 'last_login')
#
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()