from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def about_us(request):
    return render(request, 'home/about_us.html')