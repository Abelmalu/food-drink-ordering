from django.shortcuts import render,redirect
from .models import *
from .forms import *
from .filters import *

# Create your views here.



def home(request):
    
    foods = Food.objects.all().order_by('name')
    drinks = Drink.objects.all().order_by('name')
    context = {
        'foods':foods,
        'drinks':drinks
    }
    
    return render(request,'orders/index.html',context)




def order_food(request):
    if request.method == 'POST':
        order =OrderForm(request.POST)
        if order.is_valid():
            instance = order.save(commit=False)
            
            instance.customer = request.user
            instance.save()

            return redirect('orders:my_order')




    form = OrderForm()
    context = {
        'form':form

    }

    return render(request, 'orders/order_food.html',context)




def order_drink(request):
    if request.method == 'POST':
        order =DrinkForm(request.POST)
        if order.is_valid():
           instance = order.save(commit=False)
            
           instance.customer = request.user
           instance.save()
           return redirect('orders:my_order')




    form = DrinkForm()
    context = {
        'form':form

    }

    return render(request, 'orders/order_drink.html',context)




def my_order(request):
   
    orders = request.user.orderfood_set.all()
    orders_drink = request.user.orderdrink_set.all()

    context = {
        'orders':orders,
        'orders_drink':orders_drink

    }
    return render(request, 'orders/my_orders.html',context)





def all_orders(request):
    ordered_foods = OrderFood.objects.all()
    ordered_drinks = OrderDrink.objects.all()

    context = {
        'ordered_foods':ordered_foods,
        'ordered_drinks':ordered_drinks

    }

    return render(request,'orders/all_orders.html',context)




def on_road(request,pk):
    order = OrderDrink.objects.get(id=pk)
    order.status= True
    order.save()
    print(order.on_road)
    return redirect('orders:all_order')



def delivered(request,pk):
    order = OrderFood.objects.get(id=pk)
    order.status= True
    order.save()
    
    return redirect('orders:all_order')