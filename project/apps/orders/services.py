from django.db import transaction
from apps.cart.models import CartItem
from .models import Order, OrderItem

def create_order_from_cart(user):
    cart_item = CartItem.objects.filter(user=user)

    if not cart_item.exists():  # проверка корзины на пустоту
        return None

    with transaction.atomic():  # транзакция для того, чтобы предотвратит создание "полузаказов"
        order = Order.objects.create(user=user, order_price=0)

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

    return order