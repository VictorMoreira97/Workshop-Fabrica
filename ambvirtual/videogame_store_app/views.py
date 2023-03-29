from django.shortcuts import render
from .models import Jogo
from serializer import JogoSerializer
from .models import Loja
# Create your views here.
class JogoViewSet(views.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
class LojaViewSet(views.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer