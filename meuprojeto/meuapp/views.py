from django.shortcuts import render, redirect
from .forms import PessoaForm
from .models import Pessoa

def home(request):
    return render(request, 'meuapp/home.html')

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
