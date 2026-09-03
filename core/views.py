from django.shortcuts import render
from .models import Servico, Contato

def home(request):
    servicos = Servico.objects.filter(ativo=True).order_by('ordem')
    return render(request, 'core/home.html', {'servicos': servicos})