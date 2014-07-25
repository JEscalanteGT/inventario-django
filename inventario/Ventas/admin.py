from django.contrib import admin
from .models import Cliente, Venta, DetalleVenta
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellidos','nit','direccion','telefono')
	search_fields = ('nombre','apellidos','nit','direccion','telefono')

class DetalleVentaInline(admin.TabularInline):
	model = DetalleVenta
	raw_id_fields = ('producto',)
	exclude = ('precio',)
	extra = 0

class VentaAdmin(admin.ModelAdmin):
	list_display = ('id','total','fecha','cliente','usuario',)
	list_display_links = ('id','total','fecha',)
	list_filter = ('cliente','usuario','fecha',)
	search_fields = ('total','cliente__nombre','cliente__apellidos','cliente__nit',)
	readonly_fields = ('total',)
	exclude = ('usuario',)
	inlines = (DetalleVentaInline,)

	def save_model( self, request, obj, form, change ):
		obj.usuario = request.user
		obj.save()

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venta, VentaAdmin)
