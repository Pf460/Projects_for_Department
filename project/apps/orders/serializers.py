from rest_framework import serializers
from .models import Order

class  OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'products', 'order_price']

    def get_products(self, obj):
        return [item.product.id for item in obj.items.all()]
