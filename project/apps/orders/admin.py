from django.contrib import admin
from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_price', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user', )
    ordering = ('user', '-created_at')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'price')
    list_filter = ('order', 'product')
