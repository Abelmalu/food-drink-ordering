import django_filters
from .models import *

class FoodFilter(django_filters.FilterSet):
    class Meta:
        model = Food
        fields = '__all__'
        exclude = [
            'picture'
        ]