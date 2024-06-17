from django.contrib import admin
from .models import Bunk, Room, Member
# Register your models here.

admin.site.register(Bunk)
# admin.site.register(Room)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined', 'last_login', 'is_active', 'is_staff')
    search_fields = ('email',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()