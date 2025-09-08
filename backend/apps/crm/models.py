from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
import uuid



MEXICO_STATES = [
    ("AGU", "Aguascalientes"),
    ("BCN", "Baja California"),
    ("BCS", "Baja California Sur"),
    ("CAM", "Campeche"),
    ("CHP", "Chiapas"),
    ("CHH", "Chihuahua"),
    ("COA", "Coahuila"),
    ("COL", "Colima"),
    ("DIF", "Ciudad de México"),
    ("DUR", "Durango"),
    ("GUA", "Guanajuato"),
    ("GRO", "Guerrero"),
    ("HID", "Hidalgo"),
    ("JAL", "Jalisco"),
    ("MEX", "México"),
    ("MIC", "Michoacán"),
    ("MOR", "Morelos"),
    ("NAY", "Nayarit"),
    ("NLE", "Nuevo León"),
    ("OAX", "Oaxaca"),
    ("PUE", "Puebla"),
    ("QUE", "Querétaro"),
    ("ROO", "Quintana Roo"),
    ("SLP", "San Luis Potosí"),
    ("SIN", "Sinaloa"),
    ("SON", "Sonora"),
    ("TAB", "Tabasco"),
    ("TAM", "Tamaulipas"),
    ("TLA", "Tlaxcala"),
    ("VER", "Veracruz"),
    ("YUC", "Yucatán"),
    ("ZAC", "Zacatecas"),
]

# Create your models here.
class Customer(models.Model):
    sobis_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name="customers"
    )
    sobis_username = models.CharField(max_length=255, blank=True, null=True)  # copia del username
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    between_street = models.CharField(max_length=255, blank=True, null=True)
    num_ext = models.CharField(max_length=10, blank=True, null=True)
    num_int = models.CharField(max_length=10, blank=True, null=True)
    cologne = models.CharField(max_length=100, blank=True, null=True)
    municipality = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(
        max_length=3,
        choices=MEXICO_STATES,
        default="DIF",
        verbose_name="Estado",
        blank=True, null=True
    )
    country = models.CharField(max_length=100, default="México")
    rfc = models.CharField(max_length=13, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if self.sobis_user:  # guarda el username del user actual
            self.sobis_username = self.sobis_user.get_username()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name

   
PROJECT_STATUS = [
    ("NEW", "Nuevo"),
    ("APPROVED", "Aprobado"),
    ("DESIGN", "Diseño"),
    ("DEVELOPMENT", "Programación"),
    ("DEPLOYMENT", "Despliegue"),
    ("COMPLETED", "Completado"),
    ("ARCHIVED", "Archivado"),
]

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='projects')
    status = models.CharField(
        max_length=20,
        choices=PROJECT_STATUS,
        default="NEW",
        verbose_name="Estatus"
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_method = models.CharField(
        max_length=50,
        choices=[
            ('credit_card', 'Tarjeta de crédito'),
            ('paypal', 'PayPal'),
            ('mp', 'Mercado Pago'),
            ('transfer', 'Transferencia'),
            ('cash', 'Efectivo'),
        ],
        default='credit_card'
    )
    terms = models.TextField(blank=True, null=True)
    accepted_terms = models.BooleanField(default=False)
    quote = models.FileField(upload_to='quotes/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    categories = models.ManyToManyField(Category, related_name="projects", blank=True)
    #category many2many (productos sobis [crm,landing, marketing, branding, erp])
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.debt = self.total - self.paid
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
        
