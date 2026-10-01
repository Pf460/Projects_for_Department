from rest_framework import serializers
from .models import CartItem

class ProductInfoSerializer(serializers.ModelSerializer): #Класс с полями
    product_id = serializers.IntegerField(source='product.id', read_only=True)
    title = serializers.CharField(source='product.title', read_only=True)
    description = serializers.CharField(source='product.description', read_only=True)
    price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True,)

    class Meta:
        fields = ['product_id', 'title', 'description', 'price']

class CartItemSerializer(ProductInfoSerializer): #Нвследованный класс от ProductInfoSerializer
    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'title', 'description', 'price']