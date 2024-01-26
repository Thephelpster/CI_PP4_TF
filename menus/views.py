from django.shortcuts import render

from .models import Food
from .models import Drink

# Create your views here.

def menu(request):
    return render(request, 'menus/menu.html')

def food_menu(request):
    food_list = Food.objects.all()
    return render(
        request, 'menus/food_menu.html', {'food_list': food_list})

def drink_menu(request):
    drink_list = Drink.objects.all()
    return render(
        request, 'menus/drink_menu.html', {'drink_list': drink_list})