from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cachorro
from django.urls import reverse_lazy
from .forms import CachorroForm



class HelloView(View):
    def get(self, request):
        return HttpResponse('Boa tarde')
    
class CachorroListView(ListView):
    model = Cachorro
    template_name = "list_dog.html"
    context_object_name = "cachorros"

class CachorroCreateView(CreateView):
    model = Cachorro   
    form_class = CachorroForm
    template_name = "criarcachorro.html"
    success_url = reverse_lazy("listar_cachorros")

class CachorroUpdadeView(UpdateView):
    model = Cachorro
    form_class = CachorroForm
    template_name = "criarcachorro.html"
    context_object_name = ("cachorro")
    success_url = reverse_lazy("listar_cachorros")


class CachorroDeleteView(DeleteView):
    model = Cachorro
    template_name = ("deletarcachorro.html")
    context_object_name = ("cachorro")
    success_url = reverse_lazy("listar_cachorros")





# Create your views here.
