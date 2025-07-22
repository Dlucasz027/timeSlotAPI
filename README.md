###API TIME SLOT 
DESCRIÇÃO GERAL: CLIENTES = CADSTR DE CLIENTES
HORÁRIOS = HORÁRIOS DISPONÍVEIS
VINCULO ENTRE CLIENTES E HORÁRIOS



###ROTAS DA API:
CLIENTES = MANIPULAÇÃO DE DADOS DOS CLIENTES
HORÁRIOS = MANIPULAÇÃO DOS HORARIOS DISPONÍVEIS OU NÃO
VINCULO = VINCULO ENTRE CLIENTES E HORÁRIOS

/cliente/{id}/horário/  -  HORÁRIO DE UM CLIENTE ESPECÍFICO
/horário/{id}/vinculo/ - HORÁRIO VINCULADO A UM CLIENTE ESPECIFICO


###VISUALIZAÇÃO DA API
PÁGINA PADRÃO GERADA PELO DEFAULT ROUTER DO DJANGO REST FRAMEWORK QUE LISTA LINKS PARA OS RECURSOS CLIENTES, HORÁRIOS E VINCULOS.
A API DEVE RESPONDER COM OBJETOS JSON CONTENDO ESSE LINKS.


### FUNCIONALIDADES FUTURAS (para próximas versões)

- Bloqueio de horários (ex: domingos e feriados).
- Validação para evitar conflitos de agendamento no mesmo horário.
- Filtros para buscas por cliente, data ou horários livres.
- Campo “cancelado” para permitir remarcação sem deletar vínculo.
- Autenticação para multiusuários
