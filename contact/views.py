from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import ContactUsForm



def get_user_instance(request):

    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


class ContactUsMessage(View):
    template_name = 'contact/contact.html'
    success_message = 'Message has been sent.'

    def get(self, request,):
        if request.user.is_authenticated:
            email = request.user.email
            contact_form = ContactUsForm(initial={'email': email})
        else:
            contact_form = ContactUsForm()
        return render(request, 'contact/contact.html',
                      {'contact_form': contact_form})

    def post(self, request):
        contact_form = ContactUsForm(data=request.POST)

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(
                request, "Message has been sent")
            return render(request, 'contact/received.html')

        return render(request, 'contact/contact.html',
                      {'contact_form': contact_form})
