from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save, pre_save
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from Pedidos.models import actualizarSaldo

class Cliente(models.Model):
    nombre = models.CharField(max_length=45, blank=False)
    apellidos = models.CharField(max_length=45, blank=False)   
    nit = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=140, blank=True)
    telefono = models.CharField(max_length=12, blank=False)

    def __unicode__(self):
        return "%s - %s, %s" % (self.nit, self.nombre, self.apellidos)

class Venta(models.Model):
    total = models.DecimalField(default=0.00,max_digits=8, decimal_places=2, blank=False)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User)
    cliente = models.ForeignKey('cliente')

class DetalleVenta(models.Model):
    producto = models.ForeignKey('Productos.ProductoPresentacion')
    cantidad = models.PositiveIntegerField(blank=False)
    descuento = models.DecimalField(default=0.00, max_digits=2, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(1.00)], blank=False)    
    precio = models.DecimalField(default=0.00, max_digits=8, decimal_places=2, blank=False)
    venta = models.ForeignKey('venta')

def actualizarPrecio(sender, instance, **kwargs):
  instance.precio = instance.producto.precioVenta
  try:
    detalle = DetalleVenta.objects.get(id=instance.id)
    instance.venta.total -= actualizarSaldo(detalle.cantidad, detalle.precio, detalle.descuento)
    instance.venta.save()
  except DetalleVenta.DoesNotExist:
    detalle = None
    
def actualizarVenta(sender, instance, created, **kwargs):
    venta = Venta.objects.get(id=instance.venta.id)
    venta.total += actualizarSaldo(instance.cantidad, instance.precio, instance.descuento)
    venta.save()

#def actualizarUnidades(sender, instance, **kwargs):
#    try:
#        pedido = Pedido.objects.get(id=instance.id)
#        if pedido.entregado == False and instance.entregado == True:
#            detalles = DetallePedido.objects.filter(pedido=pedido)
#            for detalle in detalles:
#                detalle.producto.cantidad += detalle.cantidad
#                detalle.producto.save()
#        if pedido.entregado == True and instance.entregado == False:
#            instance.entregado = True
#    except:
#        pedido = None

pre_save.connect(actualizarPrecio, sender=DetalleVenta)
post_save.connect(actualizarVenta, sender=DetalleVenta)
#pre_save.connect(actualizarUnidades, sender=Pedido)