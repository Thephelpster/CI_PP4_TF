from django.urls import path

from menus import views

urlpatterns = [
    path('food_menu', views.food_menu, name='food_menu'),
]