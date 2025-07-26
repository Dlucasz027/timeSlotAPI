# ⏰ API TIME SLOT | Time Slot API

---

## 🇧🇷 Bem-vindo à API TIME SLOT!

Este projeto consiste em uma API REST desenvolvida com Django REST Framework para gerenciar agendamento de clientes e horários.  
A API permite o cadastro simplificado de clientes, o vínculo entre clientes e horários, além do bloqueio de horários para descanso, almoço e afins — garantindo que ninguém trabalhe 24 horas por dia!

Foram criadas rotas para manipulação de clientes, horários, vínculos entre eles e bloqueios, todas retornando dados em formato JSON para facilitar integrações futuras com frontends ou apps móveis.

## 🇺🇸 Welcome to the TIME SLOT API!

This project is a REST API built with Django REST Framework to manage client scheduling and time slots.  
The API allows simplified client registration, linking clients with available time slots, and blocking time for breaks, lunch, and rest — ensuring no one works 24/7!

Routes were created for managing clients, schedules, their links, and time blocks, all returning JSON data to facilitate future integrations with frontends or mobile apps.

---

## 📦 Conteúdos | Contents

🇧🇷
Este projeto é ideal para quem quer:
- Aprender sobre construção de APIs REST com Django REST Framework
- Manipular dados relacionados a agendamento (clientes, horários, vínculos)
- Implementar lógica de bloqueios para horários indisponíveis
- Trabalhar com rotas e visualização de dados em JSON
- Testar API com ferramentas como Postman ou Insomnia

🇺🇸
This project is ideal for those who want to:
- Learn how to build REST APIs with Django REST Framework
- Manage scheduling data (clients, time slots, links)
- Implement logic for blocking unavailable times
- Work with routes and JSON data visualization
- Test APIs using tools like Postman or Insomnia

---

## 🧰 Tecnologias Utilizadas | Technologies Used

🇧🇷
- Python
- Django
- Django REST Framework
- SQLite (padrão para desenvolvimento)
- Postman (para testes manuais da API)

🇺🇸
- Python
- Django
- Django REST Framework
- SQLite (default for development)
- Postman (for manual API testing)

---

## 🚀 Endpoints principais | Main Endpoints

| Método | Rota                  | Descrição                                      |
|--------|-----------------------|-----------------------------------------------|
| GET    | `/api/clientes/`       | Lista todos os clientes                        |
| POST   | `/api/clientes/`       | Cria um novo cliente                           |
| GET    | `/api/horarios/`       | Lista horários disponíveis                      |
| POST   | `/api/horarios/`       | Cria um novo horário                           |
| GET    | `/api/vinculos/`       | Lista vínculos entre clientes e horários      |
| POST   | `/api/vinculos/`       | Cria vínculo entre cliente e horário           |
| GET    | `/api/bloqueios/`      | Lista bloqueios de horários (ex: almoço)       |
| POST   | `/api/bloqueios/`      | Cria novo bloqueio                             |
| GET    | `/api/cliente/{id}/horario/` | Horários vinculados a um cliente específico    |
| GET    | `/api/horario/{id}/vinculo/` | Vínculo de um horário específico com cliente   |

---

## O Que Eu Aprendi | What I Learned
🇧🇷
Durante o desenvolvimento desta API, aprendi a:

- Criar APIs REST com Django REST Framework
- Estruturar modelos para relacionar clientes, horários e vínculos
- Implementar bloqueios de horários para garantir descansos
- Utilizar rotas específicas para recursos relacionados
- Testar APIs com ferramentas como Postman
- Retornar dados em JSON de forma organizada e padronizada

🇺🇸
While developing this API, I learned to:

- Build REST APIs using Django REST Framework
- Structure models linking clients, schedules, and links
- Implement time blocks to ensure breaks
- Use nested routes for related resources
- Test APIs using tools like Postman
- Return JSON data in an organized and standardized way
