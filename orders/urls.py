
from django.urls import path
from .import views

app_name = 'orders'
urlpatterns = [
    path('',views.home, name='home'),
    path('order_food/',views.order_food, name='order'),
    path('orders_drink/',views.order_drink, name='Dorder'),
    path('my_order/',views.my_order, name='my_order'),
    path('all_order/',views.all_orders, name='all_order'),
    path('on_road/<str:pk>/', views.on_road, name='on_road'),
    path('delivered/<str:pk>', views.delivered, name='delivered'),

]