from django.db import models


# Create your models here.


class addShopProducts(models.Model):
    Sno = models.IntegerField(primary_key=True, default=0, unique=True)
    Product_Name = models.CharField(max_length=50, default="")
    Product_Dec = models.CharField(max_length=1000, default="")
    Product_Price = models.IntegerField(default=0)
    Product_Img = models.ImageField(upload_to='static/productImg')



class Orders(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default="")
    phone = models.CharField(max_length=12, default=0)
    address = models.CharField(max_length=500, default="")
    qut = models.CharField(max_length=100, default=0)
    product_name = models.CharField(max_length=100)
    order_amount = models.CharField(max_length=100000, default=0)
    options = models.CharField(max_length=50, default="")
    razorpay_order_id = models.CharField(max_length=100, null=False, blank=False, default="")
    razorpay_payment_id = models.CharField(max_length=70, null=False, blank=False, default="")
    created_at = models.DateTimeField(auto_now_add = True)
    


class Contact_Us(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(default="")
    phone = models.CharField(max_length=12, default="")
    issue = models.CharField(max_length=100, default="")
    
