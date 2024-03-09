from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Product(models.Model):
    productID = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=12)
    stockQuantity = models.IntegerField()
    unitPrice = models.FloatField()
    productDes = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='uploads/')
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.productName


class CustomUser(AbstractUser):
    # all added attribute
    userID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    nickName = models.CharField(max_length=50)
    emailAddress = models.EmailField()
    password = models.CharField(max_length=255)
    shippingAddress = models.CharField(max_length=2000)


class Order(models.Model):
    orderID = models.IntegerField(primary_key=True)
    userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    purchaseDate = models.DateField(auto_now_add=True)
    orderAmount = models.FloatField()
    orderStatus = models.CharField(max_length=255)


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantityToBuy = models.IntegerField()
    price = models.FloatField()


class Cart(models.Model):
    cartID = models.IntegerField(primary_key=True)
    totalAmount = models.FloatField(default=0)
    userID = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    cartID = models.ForeignKey(Cart, on_delete=models.CASCADE)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantityToBuy = models.IntegerField(default=0)

