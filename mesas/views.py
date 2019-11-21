from django.shortcuts import render
from mesas.models import Mesa
from mesas.serializers import MesaSerializer
from rest_framework import viewsets

class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer