from .models import *
from django import forms



class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderFood
        fields = '__all__'
        exclude = [
            'status','customer'
        ]