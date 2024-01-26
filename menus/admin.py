from django.contrib import admin

# Register your models here.

from .models import Food
from .models import Drink

admin.site.register(Food)
admin.site.register(Drink)