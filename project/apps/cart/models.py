from django.db import models
from django.conf import settings
from apps.product.models import Product

User = settings.AUTH_USER_MODEL

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Запись в корзине'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return f'{self.user.email}:\n{self.product.title} - {self.product.description} - {self.product.price}'