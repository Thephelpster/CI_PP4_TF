from django.shortcuts import render

from .models import Food

# Create your views here.

def food_menu(request):
    food_list = Food.objects.all()
    return render(
        request, 'menus/food_menu.html', {'food_list': food_list})