from django.db import models  #Módulo para definir modelos no Django | Importing models from Django's ORM

class Cliente(models.Model):  #Modelo para representar um cliente | Client model
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nome

class Horario(models.Model):  #Modelo para representar um horário | Schedule model
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def __str__(self):
        return f"{self.data} {self.hora_inicio} - {self.hora_fim}"

class Vinculo(models.Model):  #Modelo para representar o vínculo entre cliente e horário | Link between client and schedule
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) #Foreingkey cria um vínculo entre duas tabelas | ForeignKey creates a link between two tables
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE) #Vínculo entre cliente e horário | Link between client and schedule
    cancelado = models.BooleanField(default=False) #models.BooleandField cria campos booleanos, nesse caso definindo se o vínculo foi cancelado | BooleanField to indicate if the link is canceled

    def __str__(self):
        return f"{self.cliente} - {self.horario} {'(Cancelado)' if self.cancelado else ''}" #Retorna o cliente, horário e se foi cancelado, caso não tenha sido cancelado, ele retorna vazio | Returns the client, schedule, and if it was canceled; if not canceled, it returns empty