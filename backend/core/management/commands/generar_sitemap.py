import requests
from django.core.management.base import BaseCommand
from django.urls import reverse

class Command(BaseCommand):
    help = 'Genera y actualiza el sitemap.xml'

    def handle(self, *args, **kwargs):
        # Aquí va tu lógica para la creación del sitemap, si es necesario
        self.stdout.write("Generando sitemap.xml...")

        # Enviar el ping manualmente a Google para actualizar el sitemap
        self.notify_google()

        self.stdout.write("Sitemap generado y notificado a Google.")

    def notify_google(self):
        # URL del sitemap en tu sitio
        sitemap_url = "http://localhost:8000/sitemap.xml"  # Cambia esto si es necesario
       
        # Enviar la notificación a Google
        google_ping_url = f"http://www.google.com/ping?sitemap={sitemap_url}"
        
        try:
            response = requests.get(google_ping_url)
            if response.status_code == 200:
                self.stdout.write("Notificación a Google exitosa.")
            else:
                self.stdout.write(f"Error al notificar a Google: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.stdout.write(f"Error al enviar el ping a Google: {e}")
