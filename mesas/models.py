from django.db import models

# Create your models here.
class Mesa(models.Model):
    codigo = models.CharField(max_length=10,unique=True)
    nombre = models.CharField(max_length=35,unique=True)
    disponible= models.BooleanField(default= True)
    ocupado_limpieza= models.BooleanField(default= True)
    ocupado_cliente= models.BooleanField(default= True)
    capacidad_sillas=models.IntegerField()
    calidad=models.IntegerField()
    comodidad=models.IntegerField()