from django import forms

from .models import ContactUs

class ContactUsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = ContactUs
        fields = (
            'name',
            'email',
            'message')