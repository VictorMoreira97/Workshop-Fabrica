from django.shortcuts import render
from .models import Jogo
from serializer import JogoSerializer, LojaSerializer
from .models import Loja
from rest_framework import viewsets

# Create your views here.
class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
    
class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer