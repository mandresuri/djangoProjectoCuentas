from django.db import models


# Create your models here.
class Servicios(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Preventa(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PlanCapacidad(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=150, blank=True)
    cliente = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField()
    preventa = models.ForeignKey(Preventa, on_delete=models.CASCADE)
    dias_venta = models.IntegerField()
    prob_cierre = models.FloatField()
    ciudad_entrega = models.CharField(max_length=50)
    account_manager = models.CharField(max_length=50)
    enlace_mat_cost = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=150)
    servicios = models.ManyToManyField(Servicios)
    productos = models.ManyToManyField(Productos)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

