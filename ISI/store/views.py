from django import forms
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseServerError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView

from .forms import CustomUserCreationForm
from .models import Product, Cart, CartItem, Order, OrderItem


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('frontpage')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def logout_view(request):
    logout(request)
    return redirect('frontpage')
from django.shortcuts import render


# def user_profile(request):
#     user = request.user
#     orders = Order.objects.filter(userID=user)
#
#     context = {
#         'user': user,
#         'orders': orders
#     }
#
#     return render(request, 'user_profile.html', context)
def user_profile(request):
    user = request.user
    orders = Order.objects.filter(userID_id=user.userID)

    context = {
        'user': user,
        'orders': orders
    }

    return render(request, 'user_profile.html', context)

def frontpage(request):
    products =  Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'frontpage.html',context)
#product detail
class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, productID=product_id)
        context = {
            'product': product
        }
        return render(request, 'product_detail.html', context)
#add to cart
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, productID=product_id)
    quantity = int(request.POST.get('quantity', 1))

    # 根据需要自行实现购物车逻辑，以下是一个简单示例：
    cart, created = Cart.objects.get_or_create(userID=request.user)  # 假设你使用了用户认证系统
    cart_item, created = CartItem.objects.get_or_create(cartID=cart, productID=product)
    cart_item.quantityToBuy += quantity
    cart_item.save()

    return redirect('product_detail', product_id=product_id)

#vendor
def productManagePage(request):

    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product.html', context)
#crud
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
class productCreateView(CreateView):
    model = Product
    template_name = "add_product.html"
    form_class = ProductForm

    def get_success_url(self):
        return reverse("frontpage")

#view cart items
from django.shortcuts import render
from .models import CartItem

@login_required(login_url='login')
def view_cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(cartID__userID=user)

    context = {
        'cart_items': cart_items
    }

    return render(request, 'cart.html', context)

#check——out
from django.shortcuts import render
from .models import CartItem, Cart

# def check_out(request):
#     user = request.user
#     cart = Cart.objects.get(userID=user)
#     cart_items = CartItem.objects.filter(cartID=cart)
#
#     context = {
#         'user': user,
#         'cart_items': cart_items,
#         'cart': cart,
#     }
#
#     return render(request, 'check_out.html', context)
def check_out(request):
    user = request.user
    cart = Cart.objects.get(userID=user)
    cart_items = CartItem.objects.filter(cartID=cart)

    context = {
        'user': user,
        'cart_items': cart_items,
        'cart': cart,
    }

    return render(request, 'check_out.html', context)

# from django.shortcuts import redirect
#
# def create_order(request):
#     cart = Cart.objects.get(userID=request.user)
#     cart_items = cart.cartitem_set.all()
#
#     # 创建订单
#     order = Order.objects.create(userID=request.user, orderAmount=cart.totalAmount, orderStatus="Pending")
#
#     # 创建订单项
#     for cart_item in cart_items:
#         OrderItem.objects.create(orderID=order, productID=cart_item.productID, quantityToBuy=cart_item.quantityToBuy, price=cart_item.productID.unitPrice)
#
#     # 清空购物车
#     cart.delete()
#
#     return redirect('cart.html')

# ok but only one
# from django.shortcuts import redirect
#
# def create_order(request):
#     cart = Cart.objects.get(userID=request.user)
#     cart_items = cart.cartitem_set.all()
#
#     # 创建订单
#     order = Order(userID=request.user, orderAmount=cart.totalAmount, orderStatus="Pending")
#     order.save()
#
#     # 创建订单项
#     for cart_item in cart_items:
#         order_item = OrderItem(orderID=order, productID=cart_item.productID, quantityToBuy=cart_item.quantityToBuy, price=cart_item.productID.unitPrice)
#
#
#     # 清空购物车
#     cart.delete()
#
#     return redirect('cart.html')

from django.db import transaction


def create_order(request):
    cart = Cart.objects.get(userID=request.user)
    cart_items = cart.cartitem_set.all()

    # 创建订单
    order = Order(userID=request.user, orderAmount=cart.totalAmount, orderStatus="Pending")
    order.save()
    with transaction.atomic():

        # 将购物车中的购物项添加到订单中
        for cart_item in cart_items:
            order_item = OrderItem(
                order_ID=order,
                productID=cart_item.productID,
                quantityToBuy=cart_item.quantityToBuy,
                price=cart_item.productID.unitPrice
            )
            order_item.save()

        # 清空购物车
    cart.delete()

    return redirect('cart.html')


