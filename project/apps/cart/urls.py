from django.urls import path
from .views import AddCartItem, ListCartItems, RemoveCartItem

urlpatterns = [
    path('cart/<int:product_id>', AddCartItem.as_view(), name='cart/<int:product_id>'),
    path('cart', ListCartItems.as_view(), name='cart'),
    path('cart/<int:id>', RemoveCartItem.as_view(), name='cart/<int:id>'),
]