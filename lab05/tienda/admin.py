from django.contrib import admin
from .models import Categoria, Producto, Cliente

# Define the custom action function
def actualizar_stock_a_20(modeladmin, request, queryset):
    # Actualiza el stock de todos los productos en el queryset a 20 unidades
    queryset.update(stock=20)

# Configura la descripción de la acción
actualizar_stock_a_20.short_description = "Actualizar stock a 20 unidades"

# Register the custom action
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    actions = [actualizar_stock_a_20]  # Añade la acción al modelo de administración de Producto

# Register other models
admin.site.register(Categoria)
admin.site.register(Cliente)
