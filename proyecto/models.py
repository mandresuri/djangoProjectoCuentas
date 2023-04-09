from django.db import models


# Create your models here.
class Servicios(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
