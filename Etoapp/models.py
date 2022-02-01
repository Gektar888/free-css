
from django.db import models

# Create your models here.

class Cars(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=50)

    def __str__(self):
        return

car = [
    ('pickup', 'Pickup'),
    ('sedan', 'Sedan'),
    ('universal', 'Universal')

]

class Order(models.Model):
    car_type = models.CharField(max_length=50, choices=car)
    drop = models.CharField(max_length=50)
    when = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.car_type}{self.drop}"