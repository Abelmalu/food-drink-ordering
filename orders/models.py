from django.db import models
from django.contrib.auth.models import User

    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    date_crreated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return str(self.user)














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
        customer = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
        food = models.ForeignKey(Food, on_delete=models.CASCADE)
        quantity = models.PositiveSmallIntegerField()
        status = models.BooleanField(default=False)
        on_road = models.BooleanField(default=False)

        def __str__(self) -> str:
          return self.food.name

    

class OrderDrink(models.Model):
        STATUS = (
            ('Pending', 'Pending'),
            ('out of delivery', 'out of delivery'),
            ('Delivered', 'Delivered'),

        )
        customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
        Drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
        quantity = models.PositiveSmallIntegerField()
        status = models.BooleanField(default=False)
        on_road = models.BooleanField(default=False)

        def __str__(self) -> str:
          return self.Drink.name

    


