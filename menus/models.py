from django.db import models

# Create your models here.

TYPE_OF_FOOD = ((0, 'Bajoran'), (1, 'Klingon'), (2, 'Talaxian'), (3, 'Mix'))
TYPE_OF_DRINK = ((0, 'Ales'), (1, 'Wines'), (2, 'Coffees'), (3, 'Teas'))

class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(
        max_length=50,
        unique=True
        )
    description = models.CharField(
        max_length=300,
        unique=True
        )
    price = models.FloatField()
    type_of_food = models.IntegerField(
        choices=TYPE_OF_FOOD,
        default=3
        )
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ['-type_of_food']

    def __str__(self):
        return self.food_name
    
class Drink(models.Model):
    drink_id = models.AutoField(primary_key=True)
    drink_name = models.CharField(
        max_length=50,
        unique=True
        )
    description = models.CharField(
        max_length=300,
        unique=True
        )
    price = models.FloatField()
    type_of_drink = models.IntegerField(
        choices=TYPE_OF_DRINK,
        default=3
        )
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ['-type_of_drink']

    def __str__(self):
        return self.drink_name