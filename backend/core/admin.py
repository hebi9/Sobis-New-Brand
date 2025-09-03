from django.contrib import admin
from .models import Page, WhoWeAre, Methodology

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(WhoWeAre)
admin.site.register(Methodology)
