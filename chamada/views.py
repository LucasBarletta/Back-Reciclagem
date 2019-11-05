from django.shortcuts import render
from rest_framework import viewsets, serializers
# Create your views here.
from chamada.models import Chamada
from chamada.serializers import ChamadaSerializer


class ChamadaViewSet(viewsets.ModelViewSet):
    queryset = Chamada.objects.all()
    # permission
    # token
    serializer_class = ChamadaSerializer