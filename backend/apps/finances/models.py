from django.db import models
from django.contrib.auth import get_user_model 
from django.utils import timezone  # Importa timezone

# Create your models here.

User = get_user_model()

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Payment_method(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Finances(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    create = models.DateField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    payment_method = models.ForeignKey(Payment_method, on_delete=models.PROTECT)
    note = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=10, choices=[('Expense', 'Gasto'), ('Income', 'Ingreso')], default='Expense', null=True, blank=True)
    
    def __str__(self):
        return f'{self.amount}'
    
    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'
        ordering = ['-create']
