from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title', 'description', 'price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description', 'price')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)