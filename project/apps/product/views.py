from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.user.permissions import IsAdmin

from .models import Product
from .serializers import ProductSerializer

class ProductList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class AdminProductAdd(APIView):
    permission_classes = [IsAdmin]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"id": serializer.data["id"], "message": "Product added"},
            status=status.HTTP_201_CREATED
        )

class AdminProductDetail(APIView):
    permission_classes = [IsAdmin]

    def patch(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def delete(self,request, id):
        product = get_object_or_404(Product, id=id)
        product.delete()
        return Response(
            {"message": "Product removed"},
            status=status.HTTP_200_OK
        )



