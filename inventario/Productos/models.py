from django.db import models
from Pedidos.models import Proveedor

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=45, blank=False)
    anulado = models.BooleanField(default=False)

class Marca(models.Model):
    nombre = models.CharField(max_length=45, blank=False)
    anulado = models.BooleanField(default=False)

class Presentacion(models.Model):
    nombre = models.CharField(max_length=45, blank=False)
    anulado = models.BooleanField(default=False)

class Producto(models.Model):
    nombre = models.CharField(max_length=140, blank=False)
    anulado = models.BooleanField(default=False)
    categoria = models.ForeignKey('Categoria')
    marca = models.ForeignKey('Marca')
    proveedor = models.ForeignKey(Proveedor)

class ProductoPresentacion(models.Model):
    precioVenta = models.DecimalField(default=0.00, decimal_places=2, max_digits=8, blank=False)
    cantidad = models.PositiveIntegerField(blank=False)
    anulado = models.BooleanField(default=False)
    producto = models.ForeignKey('Producto')
    presentacion = models.ForeignKey('presentacion')