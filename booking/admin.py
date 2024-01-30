from django.contrib import admin

# Register your models here.

from .models import Table, Booking


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_id', 'table_name', 'max_seats')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = (
        'user',
        'name',
        'email',
        'guest_count',
        'status',
        'table_id',
        'requested_date',
        'requested_time',
        'created_date'
        )
    list_display = (
        'booking_id',
        'user',
        'name',
        'guest_count',
        'status',
        'table',
        'requested_date',
        'requested_time',
        'created_date')

    search_fields = ['guest__name']
    actions = ['confirm_booking']

    def confirm_bookings(self, queryset):
        queryset.update(status='Booking Confirmed')