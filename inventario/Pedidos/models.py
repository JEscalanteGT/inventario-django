from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save, pre_save
from django.core.exceptions import ObjectDoesNotExist
from Productos.models import Producto

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
    proveedor = models.ForeignKey('proveedor')
    total = models.DecimalField(default=0.00,max_digits=8, decimal_places=2, blank=False)
    fechaPedido = models.DateTimeField(auto_now_add=True)
    fechaIngreso = models.DateTimeField(blank=True, null=True)
    entregado = models.BooleanField(default=False)

class DetallePedido(models.Model):
    producto = models.ForeignKey('Productos.ProductoPresentacion')
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad (unidades)",blank=False)
    precio = models.DecimalField(verbose_name="Costo por unidad (Q)",default=0.00, max_digits=8, decimal_places=2, blank=False)
    descuento = models.DecimalField(verbose_name="Descuento",default=0.00, max_digits=2, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(1.00)], blank=False)    
    pedido = models.ForeignKey('pedido')

def actualizarSaldo(cantidad, precio, descuento):
    totalMercaderia = (cantidad * precio)
    descuento = totalMercaderia * descuento
    return totalMercaderia - descuento

def actualizarPrecio(sender, instance, **kwargs):
  instance.precio = instance.producto.precioCosto
  try:
    detalle = DetallePedido.objects.get(id=instance.id)
    if not detalle.pedido.entregado:
        instance.pedido.total -= actualizarSaldo(detalle.cantidad, detalle.precio, detalle.descuento)
        instance.pedido.save()
  except DetallePedido.DoesNotExist:
    detalle = None
    
def actualizarPedido(sender, instance, created, **kwargs):
    pedido = Pedido.objects.get(id=instance.pedido.id)
    if not pedido.entregado:
        pedido.total += actualizarSaldo(instance.cantidad, instance.precio, instance.descuento)
        pedido.save()

def actualizarUnidades(sender, instance, **kwargs):
    try:
        pedido = Pedido.objects.get(id=instance.id)
        if pedido.entregado == False and instance.entregado == True:
            detalles = DetallePedido.objects.filter(pedido=pedido)
            for detalle in detalles:
                detalle.producto.cantidad += detalle.cantidad
                detalle.producto.save()
        if pedido.entregado == True and instance.entregado == False:
            instance.entregado = True
    except:
        pedido = None

post_save.connect(actualizarPedido, sender=DetallePedido)
pre_save.connect(actualizarPrecio, sender=DetallePedido)
pre_save.connect(actualizarUnidades, sender=Pedido)