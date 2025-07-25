from rest_framework import serializers  # Importa o módulo serializers do Django REST Framework | Import the serializers module from Django REST Framework
from .models import Cliente, Horario, Vinculo, BloqueioHorario  # Importa os modelos que serão serializados | Import the models to be serialized

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:   # Classe interna que define configurações do serializer | Internal class that defines serializer configurations
        model = Cliente  # Modelo que será serializado | Model to be serialized
        fields = '__all__'  # Campos que serão incluídos no JSON | Fields to be included in the JSON

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

def validate(self, data):
    data_horario = data['data']
    hora_inicio = data['hora_inicio']
    hora_fim = data['hora_fim']

    bloqueios = BloqueioHorario.objects.filter(data=data_horario)  # Filtro de bloqueios apenas para a data validada | Filter blockings only for the validated date

    for bloqueio in bloqueios:
        if (hora_inicio < bloqueio.hora_fim and hora_fim > bloqueio.hora_inicio):
            raise serializers.ValidationError(
                f"Horário sobrepõe o bloqueio: {bloqueio}"
            )

    return data

class VinculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vinculo
        fields = '__all__'

    def validate(self, data):
        horario = data['horario']

        data_horario = horario.data
        hora_inicio = horario.hora_inicio
        hora_fim = horario.hora_fim

        bloqueios = BloqueioHorario.objects.filter(data=data_horario)

        for bloqueio in bloqueios:
            if (hora_inicio < bloqueio.hora_fim and hora_fim > bloqueio.hora_inicio):
                raise serializers.ValidationError(
                    f"O horário selecionado está bloqueado: {bloqueio}"
                )

        return data

class BloqueioHorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloqueioHorario
        fields = '__all__'