from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.user.permissions import IsClient
from django.shortcuts import get_object_or_404


from apps.product.models import Product
from .models import CartItem
from .serializers import CartItemSerializer

class DetailCartItem(APIView):
    permission_classes = [IsClient]

    def post(self, request, id):
        product = get_object_or_404(Product, id=id)
        CartItem.objects.create(user=request.user, product=product)
        return Response(
            {'message': 'Product add to card'},
            status=status.HTTP_201_CREATED
        )

    def delete(self, request, id):
        cart_item = get_object_or_404(CartItem, id=id)
        if cart_item.user != request.user:
            return Response(
                {'message': 'Forbidden for you'},
                status=status.HTTP_403_FORBIDDEN
            )
        else:
            cart_item.delete()
            return Response(
                {'message': 'Item removed from cart'},
                status=status.HTTP_200_OK
            )

class ListCartItems(APIView):
    permission_classes = [IsClient]

    def get(self,request):
        cart_items = CartItem.objects.filter(user=request.user.id)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

