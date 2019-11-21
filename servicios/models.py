from django.db import models

# Create your models here.
class Servicio(models.Model):
    mesa= models.ForeignKey("mesas.Mesa",  on_delete=models.CASCADE)
    id_cliente = models.CharField(max_length=35)
    id_mesero=models.CharField(max_length=35)
    tiempo_llegada_cliente= models.TimeField(auto_now_add=True)
    tiempo_total_cliente=models.TimeField()
    tiempo_inicio_limpieza= models.TimeField(auto_now_add=True)
    tiempo_total_limpieza=models.TimeField()
    tiempo_total_servicio=models.TimeField()
  