from django import forms
from datetime import datetime
from .models import Booking



class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    requested_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().date()}))

    class Meta:
        model = Booking
        fields = (
            'name',
            'email',
            'guest_count',
            'table',
            'requested_date',
            'requested_time')