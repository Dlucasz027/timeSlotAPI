from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Horario, Vinculo, BloqueioHorario
from .serializers import ClienteSerializer, HorarioSerializer, VinculoSerializer, BloqueioHorarioSerializer

class ClienteViewSet(viewsets.ModelViewSet):  # ViewSet que gera automaticamente as operações CRUD (listar, criar, atualizar, deletar) | ViewSet that automatically generates CRUD operations (list, create, update, delete)
    queryset = Cliente.objects.all()  # Define o conjunto de dados que será manipulado (todos os objetos Cliente, ou qualquer que seja) | Defines the dataset to be manipulated (all Cliente objects, or whatever is applicable)
    serializer_class = ClienteSerializer   # Define qual serializer será usado para transformar os dados | Defines which serializer will be used to transform the data

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class VinculoViewSet(viewsets.ModelViewSet):
    queryset = Vinculo.objects.all()
    serializer_class = VinculoSerializer

class BloqueioHorarioViewSet(viewsets.ModelViewSet):
    queryset = BloqueioHorario.objects.all()
    serializer_class = BloqueioHorarioSerializer