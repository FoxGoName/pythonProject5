from django.apps import AppConfig
from django.db.models.signals import post_save


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'

    def ready(self):
        from .models import CartItem
        from .signals import update_cart_total_amount
        post_save.connect(update_cart_total_amount, sender=CartItem)
