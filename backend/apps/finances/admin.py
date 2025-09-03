from django.contrib import admin
from .models import Category, Payment_method,Finances
# Register your models here.

admin.site.register(Category)
admin.site.register(Payment_method)
admin.site.register(Finances)