from django.contrib import admin
from .models import Customer, Project, Category
# Register your models here.

admin.site.register(Customer)
admin.site.register(Project)
admin.site.register(Category)
