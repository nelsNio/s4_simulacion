from .models import Servicio
from django.contrib import admin


@admin.register(Servicio)
class AdminServicio(admin.ModelAdmin):
    list_display = ('id','mesa','id_cliente','id_mesero','tiempo_llegada_cliente','tiempo_total_cliente','tiempo_inicio_limpieza','tiempo_total_limpieza','tiempo_total_servicio')
  