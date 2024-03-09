
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CartItem

@receiver(post_save, sender=CartItem)
def update_cart_total_amount(sender, instance, **kwargs):
    cart = instance.cartID
    cart_items = cart.cartitem_set.all()

    total_amount = sum(item.quantityToBuy * item.productID.unitPrice for item in cart_items)
    cart.totalAmount = total_amount
    cart.save()