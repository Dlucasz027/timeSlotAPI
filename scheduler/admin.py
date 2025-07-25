from django.contrib import admin
from scheduler.models import Horario, Cliente, Vinculo, BloqueioHorario

class Clientes(admin.ModelAdmin): # Define as colunas que serão exibidas na listagem do admin | Admin interface for Cliente model
    list_display = ('id', 'nome', 'telefone')
    search_fields = ('nome',)
    ordering = ('nome',)  # Ordena os registros em ordem alfabética pelo nome | Orders records alphabetically by name

admin.site.register(Cliente, Clientes)

class Horarios(admin.ModelAdmin):
    list_display = ('id', 'data', 'hora_inicio', 'hora_fim')   # Mostra os campos definidos como colunas na listagem do admin | Admin interface for Horario model
    list_filter = ('data',)  # Adiciona um filtro lateral para filtrar por data | Adds a sidebar filter for date

admin.site.register(Horario, Horarios)

class Vinculos(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'horario', 'cancelado')
    list_filter = ('cancelado',)
    search_fields = ('cliente__nome',) # Permite buscar pelo nome do cliente associado ao vínculo | Allows searching by the name of the associated client

admin.site.register(Vinculo, Vinculos)  # Aqui temos primeiro o modelo criado em models e depois como ele será exibido no admin | Registers the Vinculo model with its admin interface

@admin.register(BloqueioHorario)
class BloqueioHorarioAdmin(admin.ModelAdmin):
    list_display = ('data', 'hora_inicio', 'hora_fim', 'descricao')
    list_filter = ('data',)
    search_fields = ('descricao',)  