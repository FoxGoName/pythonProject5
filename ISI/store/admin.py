from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Product, CustomUser, Cart, CartItem, OrderItem, Order

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(CartItem)
admin.site.register(OrderItem)

from .models import CustomUser
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('shippingAddress',)}),
    )

    list_display = ['userID','name','nickName','emailAddress',]
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)