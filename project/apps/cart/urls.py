from django.urls import path
from .views import DetailCartItem, ListCartItems

urlpatterns = [
    path('cart/<int:id>', DetailCartItem.as_view(), name='cart_item_detail'),
    path('cart', ListCartItems.as_view(), name='cart_list'),
]