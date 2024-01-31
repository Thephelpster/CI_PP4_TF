from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Name (required)',
                'id': 'name'}))
    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email (required)',
                'id': 'email'}))
    message = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Write your message (required)',
                'id': 'message'}))