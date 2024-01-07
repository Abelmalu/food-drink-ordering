from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.



def home(request):
    foods = Food.objects.all().order_by('name')
    drinks = Drink.objects.all().order_by('name')
    context = {
        'foods':foods,
        'drinks':drinks
    }
    
    return render(request,'orders/index.html',context)




def orders(request):
    if request.method == 'POST':
        order =OrderForm(request.POST)
        if order.is_valid():
            order.save()
            return redirect('orders:home')




    form = OrderForm()
    context = {
        'form':form

    }

    return render(request, 'orders/order_page.html',context)
