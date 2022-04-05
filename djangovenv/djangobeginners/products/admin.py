from django.contrib import admin

from .models import Product # relative import. Import Product class from same directory/module. 
# Register your models here.

admin.site.register(Product)
