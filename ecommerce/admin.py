from django.contrib import admin
from .models import Laptop, AddToCart, UserDetails, Payment

# Register your models here.

admin.site.register(Laptop)

admin.site.register(AddToCart)

admin.site.register(UserDetails)

admin.site.register(Payment)
