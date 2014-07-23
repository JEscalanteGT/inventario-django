from django.contrib import admin
from .models import Cliente, Venta, DetalleVenta
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellidos','nit','direccion','telefono')
	search_fields = ('nombre','apellidos','nit','direccion','telefono')

class DetalleVentaInline(admin.TabularInline):
	model = DetalleVenta
	extra = 0

class VentaAdmin(admin.ModelAdmin):
	list_display = ('id','total','fecha','cliente','usuario',)
	list_display_links = ('id','total','fecha',)
	list_filter = ('cliente','usuario','fecha',)
	search_fields = ('total','cliente__nombre','cliente__apellidos','cliente__nit',)
	inlines = (DetalleVentaInline,)

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venta, VentaAdmin)
