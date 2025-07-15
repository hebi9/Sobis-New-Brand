# core/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Page  # Suponiendo que tengas un modelo Page o algo similar

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"  # Frecuencia de cambio (opcional)
    priority = 0.5  # Prioridad (opcional)

    def items(self):
        return ['home', 'about', 'contact']  # Aquí pones las vistas que quieres incluir

    def location(self, item):
        return reverse(item)

class PageSitemap(Sitemap):
    def items(self):
        return Page.objects.all()  # Asegúrate de tener un modelo Page

    def lastmod(self, obj):
        return obj.updated_at  # Si tienes un campo de actualización

    def location(self, obj):
        return reverse('page_detail', args=[obj.slug])  # Ruta de detalles de página
