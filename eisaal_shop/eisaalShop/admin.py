from django.contrib import admin
from .models import addShopProducts, Orders, Contact_Us

# Register your models here.

admin.site.register(addShopProducts)
admin.site.register(Orders)
admin.site.register(Contact_Us)
