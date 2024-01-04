from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    name = models.CharField(max_length = 255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)



    def __str__(self) -> str:
          return self.name
    



class Food(models.Model):

   
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.PositiveBigIntegerField()
    ingredients = models.CharField(max_length=255)
    picture = models.ImageField(null=True)

    def __str__(self) -> str:
        return self.name


class Drink(models.Model):
    CATEGORY = (
        ('SOFT', 'SOFT DRINK'),
        ('ALCOHOL', 'ALCOHOL DRINK'),

    )
   
    name=models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY )
    picture = models.ImageField(null=True)

    def __str__(self) -> str:
        return self.name






class OrderFood(models.Model):
        STATUS = (
            ('Pending', 'Pending'),
            ('out of delivery', 'out of delivery'),
            ('Delivered', 'Delivered'),

        )
        customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
        quantity = models.PositiveSmallIntegerField()
        price = models.FloatField()
        status = models.CharField(max_length=255, choices=STATUS)

        def __str__(self) -> str:
          return self.name

    

class OrderDrink(models.Model):
        STATUS = (
            ('Pending', 'Pending'),
            ('out of delivery', 'out of delivery'),
            ('Delivered', 'Delivered'),

        )
        customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
        quantity = models.PositiveSmallIntegerField()
        price = models.FloatField()
        status = models.CharField(max_length=255, choices=STATUS)

        def __str__(self) -> str:
          return self.name

    


