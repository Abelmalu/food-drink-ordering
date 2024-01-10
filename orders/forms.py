from .models import *
from django import forms



class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderFood
        fields = ['food','quantity']
       
        widgets = {
            'food': forms.Select(attrs={
                'class': "form-control form-control-lg placeholder='food'  "
            }),
            'quantity': forms.TextInput(attrs={
                'class': "form-control form-control-lg placeholder='food'  "
            }),

        }



class DrinkForm(forms.ModelForm):
    class Meta:
        model = OrderDrink
        fields = ['Drink', 'quantity']

        widgets = {
            'Drink': forms.Select(attrs={
                'class': "form-control form-control-lg placeholder='food'  "
            }),
            'quantity': forms.TextInput(attrs={
                'class': "form-control form-control-lg placeholder='food'  "
            }),

        }
