from django.contrib import admin
from .models import ContactUs

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_filter = (
        'user',
        'name',
        'email',
        'created_date'
        )
    list_display = (
        'message_id',
        'user',
        'name',
        'message',
        'created_date')