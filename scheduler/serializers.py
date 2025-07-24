from rest_framework import serializers  # Importa o módulo serializers do Django REST Framework | Import the serializers module from Django REST Framework
from .models import Cliente, Horario, Vinculo  # Importa os modelos que serão serializados | Import the models to be serialized

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:   # Classe interna que define configurações do serializer | Internal class that defines serializer configurations
        model = Cliente  # Modelo que será serializado | Model to be serialized
        fields = '__all__'  # Campos que serão incluídos no JSON | Fields to be included in the JSON

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

class VinculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vinculo
        fields = '__all__'
