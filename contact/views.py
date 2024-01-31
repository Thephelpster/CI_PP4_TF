from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact(request):
    initial_data = {}
    if request.user.is_authenticated:
        name = request.user.first_name
        initial_data['name'] = name if name else request.user.username
        initial_data['email'] = request.user.email

    form = ContactForm(initial=initial_data)
    return render(request, 'contact/contact.html', {'form': form})
