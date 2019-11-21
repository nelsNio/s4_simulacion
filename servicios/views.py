from django.shortcuts import render
from servicios.models import Servicio
from servicios.serializers import ServicioSerializer
from rest_framework import viewsets

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer