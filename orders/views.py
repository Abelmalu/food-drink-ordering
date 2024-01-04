from django.shortcuts import render
from .models import *

# Create your views here.



def home(request):
    foods = Food.objects.all().order_by('name')
    context = {
        'foods':foods
    }
    
    return render(request,'orders/index.html',context)