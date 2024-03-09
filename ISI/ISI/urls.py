"""
URL configuration for ISI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from store.views import  user_profile, logout_view, check_out, SignUpView,CustomLoginView,frontpage,productManagePage,productCreateView,ProductDetailView,add_to_cart,view_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view() , name='signup'),
    path('signup/', SignUpView.as_view() , name='signup'),
    path('logout/', logout_view, name='logout'),
    path('user_profile/', user_profile, name='user_profile'),
    path('cart/', view_cart, name='view_cart'),

    path('cart/check_out', check_out, name='check_out'),
    # path('cart/create_order', create_order, name='create_order'),
    # path('cart/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    #vendor
    path('productManager/', productManagePage, name="productManager"),
    path('productManager/add/', productCreateView.as_view(), name="addProduct"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
