from django.contrib import admin
from .models import Categoria, Marca, Presentacion, Producto, ProductoPresentacion
# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	order_filter = ('nombre',)
	search_fields = ('nombre',)

class MarcaAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	order_filter = ('nombre',)
	search_fields = ('nombre',)

class PresentacionAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	order_filter = ('nombre',)
	search_fields = ('nombre',)

class PresentacionInline(admin.TabularInline):
	model = ProductoPresentacion
	extra = 0
	readonly_fields = ('cantidad',)
	verbose_name = 'presentacion'
	verbose_name_plural = 'Presentaciones de este producto'

class ProductoAdmin(admin.ModelAdmin):
	list_display = ('nombre','categoria','marca','proveedor')
	list_filter = ('categoria','marca','proveedor',)
	order_filter = ('nombre',)
	search_fields = ('nombre',)
	inlines = (PresentacionInline,)
	
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Presentacion, PresentacionAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(ProductoPresentacion)