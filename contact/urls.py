from django.urls import path

from . import views


urlpatterns = [
    path('contact/', views.ContactUsMessage.as_view(), name='contact'),
]