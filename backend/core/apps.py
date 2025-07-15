from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Configuración por defecto para campos auto-incrementales
    name = 'core' 