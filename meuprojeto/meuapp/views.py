from django.shortcuts import render, redirect
from .forms import PessoaForm
from .models import Pessoa
import requests
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'list.html', {'pessoas': pessoas})

def criar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'create.html', {'pessoa': form })

def deletar_pessoa(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('listar_pessoas')
    return render(request, 'confirmar_delete.html', {'pessoa': pessoa})

def atualizar_pessoas(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save
            return redirect('listar_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'create.html', {'pessoa': form})

def consultaCep(request):
    response = requests.get("https://viacep.com.br/ws/58328000/json/", verify=False)
    dadosEndereco = response.json()
    endereco = Pessoa.objects.create(
        nome=dadosEndereco['localidade'],
        idade=dadosEndereco['ibge'],
        email="admin@admin.com",
    )
    return HttpResponse(dadosEndereco['localidade'])
