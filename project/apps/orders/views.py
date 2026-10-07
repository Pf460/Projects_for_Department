from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.user.permissions import IsClient

from .serializers import OrderSerializer
from django.db import transaction
from apps.cart.models import CartItem
from .models import Order, OrderItem

class OrderView(APIView):
    permission_classes = [IsClient]

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        cart_item = CartItem.objects.filter(user=request.user)

        if not cart_item.exists(): #проверка корзины на пустоту
            return Response (
                {"message": "Cart is empty"},
                status = status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        with transaction.atomic(): #транзакция для того, чтобы предотвратит создание "полузаказов"
            order = Order.objects.create(user=request.user, order_price=0)

            total = 0
            for item in cart_item:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                )
                total += item.product.price
            order.order_price = total
            order.save()

            cart_item.delete()

            return Response(
                {'order_id': order.id, 'message': 'Order is proccessed'},
                status = status.HTTP_201_CREATED
            )
