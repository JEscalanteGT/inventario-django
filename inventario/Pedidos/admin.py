from django.contrib import admin
from .models import Proveedor, Pedido, DetallePedido
# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
	list_display = ('nombre','direccion','telefono')
	order_filter = ('nombre',)
	search_fields = ('nombre','direccion','telefono')

class DetallePedidoInline(admin.TabularInline):
	model = DetallePedido
	extra = 0

class PedidoAdmin(admin.ModelAdmin):
	list_display = ('id','total','fechaPedido','fechaIngreso','entregado',)
	list_display_links = ('id','total','fechaPedido','fechaIngreso',)
	#list_filter = ('proveedor',)
	order_filter = ('id',)
	search_fields = ('total','fechaPedido','fechaIngreso')
	inlines = (DetallePedidoInline,)

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Pedido, PedidoAdmin)
