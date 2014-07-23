from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#from Productos.models import ProductoPresentacion

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=45, blank=False)
    direccion = models.CharField(max_length=140, blank=True)
    telefono = models.CharField(max_length=12, blank=False)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Proveedores"

class Pedido(models.Model):
    total = models.DecimalField(default=0.00,max_digits=8, decimal_places=2, blank=False)
    fechaPedido = models.DateTimeField(auto_now_add=True)
    fechaIngreso = models.DateTimeField(blank=True, null=True)
    entregado = models.BooleanField(default=False)

class DetallePedido(models.Model):
    producto = models.ForeignKey('Productos.ProductoPresentacion')
    cantidad = models.PositiveIntegerField(blank=False)
    precio = models.DecimalField(default=0.00, max_digits=8, decimal_places=2, blank=False)
    descuento = models.DecimalField(default=0.00, max_digits=2, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(1.00)], blank=False)    
    pedido = models.ForeignKey('pedido')