from django.urls import path
from . import views
from django.contrib import admin
from .views import listar_pessoas, criar_pessoa, deletar_pessoa, atualizar_pessoas, consultaCep

urlpatterns = [
    path('', views.home, name='home'),
    path('consulta', consultaCep, name="consultacep"),
    path('listar', listar_pessoas, name='listar_pessoas'),
    path('criar', criar_pessoa, name='criar_pessoa'),
    path('delete/<int:pk>', deletar_pessoa, name='deletar_pessoa'),
    path('atualizar/<int:pk>', atualizar_pessoas, name='atualizar_pessoas')
]
