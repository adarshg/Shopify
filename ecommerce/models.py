from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Laptop(models.Model):
    image = models.ImageField(upload_to='images')
    descr = models.TextField()
    name = models.CharField(max_length = 50, null = True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name
    
class AddToCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, null = True)
    quantity = models.IntegerField(default=1)
    # razor_pay_order_id = models.CharField(max_length = 100, null = True, blank = True)
    # razor_pay_payment_id = models.CharField(max_length = 100, null = True, blank = True)
    # razor_pay_payment_signature = models.CharField(max_length = 100, null = True, blank = True)
    
    # def __str__(self):
    #     return self.laptop
    
class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    mobile = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')])
    housename = models.CharField(max_length = 50)
    area = models.CharField(max_length = 50)
    district = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    pin = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{6}$')])

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField()
    razorpay_order_id = models.CharField(max_length=100)
    razorpay_payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
