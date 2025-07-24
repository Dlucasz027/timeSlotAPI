from django.contrib import admin # Importa o módulo do Django para a área administrativa (admin) | Imports the Django module for the admin area
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),   # Define a rota /admin/ para acessar a interface administrativa do Django | Defines the /admin/ route to access the Django admin interface
    path('api/', include('scheduler.urls')),  # Inclui todas as rotas definidas no arquivo scheduler/urls.py e "prefixa" elas com 'api/', ou seja, suas rotas da API vão começar com /api/
]
