from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone  # Importa timezone

# Create your models here.

User = get_user_model()

class Streak(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    streak = models.PositiveIntegerField(default=0)
    
    def increment_streak(self):
        """ Incrementa la racha en 1 """
        self.streak += 1
        self.save()

    def reset_streak(self):
        """ Reinicia la racha a 0 """
        self.streak = 0
        self.save()

    def __str__(self):
        return f"{self.user.username} - Streak: {self.streak}"

class Relationship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estatus = models.CharField(max_length=10,choices=[('Good', 'Bien'), ('Regular', 'Regular'), ('Bad', 'Malo')], default='Good', null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    empathy = models.TextField(null=True, blank=True)
    comprehension = models.TextField(null=True, blank=True)
    curiosity = models.TextField(null=True, blank=True)
    learn_more = models.TextField(null=True, blank=True)
    learn_from_you = models.TextField(null=True, blank=True)
    miracle  = models.TextField(null=True, blank=True)
    create = models.DateField(default=timezone.now)
    dessert = models.BooleanField(default=False)
    

    def save(self, *args, **kwargs):
        # Verifica si el objeto ya existe para saber si es un nuevo registro
        is_new = self._state.adding
        
        super().save(*args, **kwargs)  # Guarda la relación primero

        # Manejo de la racha (streak)
        streak, created = Streak.objects.get_or_create(user=self.user)  # Obtiene o crea la racha del usuario

        # Solo se incrementa la racha si es un nuevo registro
        if is_new and self.estatus == 'Good':
            streak.increment_streak()  # Incrementa la racha
        elif is_new and self.estatus == 'Bad':
            streak.reset_streak()  # Reinicia la racha
            
    def __str__(self):
        return f'{self.create}'
    
    class Meta:
        verbose_name = 'Relación'
        ordering = ['-create']
        