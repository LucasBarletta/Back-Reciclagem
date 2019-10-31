from django.shortcuts import render
from rest_framework import viewsets, serializers
# Create your views here.
from noticia.models import Noticia
from noticia.serializers import NoticiaSerializer


class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    # permission
    # token
    serializer_class = NoticiaSerializer