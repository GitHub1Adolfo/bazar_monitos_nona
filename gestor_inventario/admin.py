from django.contrib import admin
from .models import Producto
# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    llist_display = ('nombre', 'categoria', 'precio')  # Campos que se mostrarán en la lista
    search_fields = ('nombre', 'categoria')  # Campos para la búsqueda
    list_filter = ('categoria',)  # Filtro por categoría
    ordering = ('nombre',)  # Ordenación por nombre