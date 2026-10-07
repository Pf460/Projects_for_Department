from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.user.permissions import IsClient
from .serializers import OrderSerializer
from .services import create_order_from_cart
from .models import Order

class OrderView(APIView):
    permission_classes = [IsClient]

    def get(self, request):
        orders = Order.objects.filter(user=request.user).prefetch_related('items__product') #prefetch подтягивает все данные из бд по продуктам со связью многие заказы ко многим продуктам
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        order = create_order_from_cart(request.user)

        if order is None:
            return Response(
                {'error':{'code': 422, 'message': 'Cart is empty'}},
                status = status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        else:
            return Response(
                {'order_id': order.id, 'message': 'Order is processed'},
                status = status.HTTP_201_CREATED
            )