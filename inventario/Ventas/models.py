from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=45, blank=False)
    apellidos = models.CharField(max_length=45, blank=False)   
    nit = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=140, blank=True)
    telefono = models.CharField(max_length=12, blank=False)
    anulado = models.BooleanField(default=False)

class Venta(models.Model):
    total = models.DecimalField(default=0.00,max_digits=8, decimal_places=2, blank=False)
    fecha = models.DateTimeField(auto_now_add=True)
    anulado = models.BooleanField(default=False)
    usuario = models.ForeignKey(User)
    cliente = models.ForeignKey('cliente')

class DetalleVenta(models.Model):
    cantidad = models.PositiveIntegerField(blank=False)
    precio = models.DecimalField(default=0.00, max_digits=8, decimal_places=2, blank=False)
    descuento = models.DecimalField(default=0.00, max_digits=2, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(1.00)], blank=False)    
    anulado = models.BooleanField(default=False)
    producto = models.ForeignKey('Productos.ProductoPresentacion')