from .models import *
from django import forms



class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderFood
        fields = '__all__'
        exclude = [
            'status','customer'
        ]



class DrinkForm(forms.ModelForm):
    class Meta:
        model = OrderDrink
        fields = '__all__'
        exclude = [
            'status','customer'
        ]