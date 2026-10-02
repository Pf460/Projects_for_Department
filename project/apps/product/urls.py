from django.urls import path
from .views import ProductList, AdminProductAdd, AdminProductDetail

urlpatterns = [
    path('products', ProductList.as_view(), name='products_list'),
    path('product', AdminProductAdd.as_view(), name='product_add'),
    path('product/<int:id>', AdminProductDetail.as_view(), name='product_detail'),

]