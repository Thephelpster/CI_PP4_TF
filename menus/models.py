from django.db import models

# Create your models here.

TYPE_OF_FOOD = ((0, 'Starters'), (1, 'Mains'), (2, 'Desserts'), (3, 'New'))

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