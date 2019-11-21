from .models import Mesa
from django.contrib import admin


@admin.register(Mesa)
class AdminMesa(admin.ModelAdmin):
    list_display = ('id','codigo','nombre','disponible','ocupado_limpieza','ocupado_cliente','capacidad_sillas','calidad','comodidad')
