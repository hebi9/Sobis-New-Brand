from django.contrib import admin
from .models import Customer, Project, Category
# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "customer", "status", "token", "created_at")
    list_display_links = ("id", "name", "customer", "status", "token", "created_at")
    search_fields = ("name", "customer__name","status", "customer__sobis_username")
    list_filter = ("status",  "customer__name","categories")
    readonly_fields = ("token",)


admin.site.register(Customer)
admin.site.register(Category)
