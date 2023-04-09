from django.db import models


# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre}"


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre}"

class Preventa(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Comercial(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"



class PlanCapacidad(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=150, blank=True)
    cliente = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField()
    preventa = models.ForeignKey(Preventa, on_delete=models.CASCADE)
    dias_venta = models.IntegerField()
    prob_cierre = models.FloatField()
    ciudad_entrega = models.CharField(max_length=50)
    comercial = models.ForeignKey(Comercial, on_delete=models.CASCADE, default=None)
    enlace_mat_cost = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=150)
    servicios = models.ManyToManyField(Servicio, blank=True)
    productos = models.ManyToManyField(Producto, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


