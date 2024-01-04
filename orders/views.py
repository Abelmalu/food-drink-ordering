from django.shortcuts import render
from .models import *

# Create your views here.



def home(request):
    foods = Food.objects.all().order_by('name')
    drinks = Drink.objects.all().order_by('name')
    context = {
        'foods':foods,
        'drinks':drinks
    }
    
    return render(request,'orders/index.html',context)