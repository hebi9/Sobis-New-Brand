from django.db import models

# Create your models here.
class Quotes(models.Model):
    author = models.CharField(max_length=255)
    case = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.case} by {self.author}" if self.author and self.case else self.author