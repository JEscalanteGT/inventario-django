from django.db import models
from Pedidos.models import Proveedor

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=45, blank=False)
    
    def __unicode__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=45, blank=False)

    def __unicode__(self):
        return self.nombre

class Presentacion(models.Model):
    nombre = models.CharField(max_length=45, blank=False)
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Presentaciones"

class Producto(models.Model):
    nombre = models.CharField(max_length=140, blank=False)
    categoria = models.ForeignKey('Categoria')
    marca = models.ForeignKey('Marca')
    proveedor = models.ForeignKey(Proveedor)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Productos"

class ProductoPresentacion(models.Model):
    presentacion = models.ForeignKey('presentacion')
    precioVenta = models.DecimalField(verbose_name="Precio de venta", default=0.00, decimal_places=2, max_digits=8, blank=False)
    producto = models.ForeignKey('Producto')
    cantidad = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return "%s - %s" % (self.producto, self.presentacion)

    class Meta:
        verbose_name = "Presentacion de producto"
        verbose_name_plural = "Presentaciones de producto"