from django.urls import path
from . import views
from django.contrib import admin
from .views import listar_pessoas, criar_pessoa

urlpatterns = [
    path('', views.home, name='home'),
    path('listar/', listar_pessoas, name='listar_pessoas'),
    path('criar/', criar_pessoa, name='criar_pessoa')
]
