from django.shortcuts import render
from .models import Servico, Contato

def home(request):
    servicos = Servico.objects.filter(ativo=True).order_by('ordem')
    return render(request, 'core/home.html', {'servicos': servicos})

def sobre(request):
    return render(request, 'core/sobre.html')

def servicos(request):
    servicos = Servico.objects.filter(ativo=True).order_by('ordem')
    return render(request, 'core/servicos.html', {'servicos': servicos})

def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        mensagem = request.POST.get('mensagem')
        Contato.objects.create(nome=nome, email=email, telefone=telefone, mensagem=mensagem)
        return render(request, 'core/contato.html', {'sucesso': True})
    return render(request, 'core/contato.html')
