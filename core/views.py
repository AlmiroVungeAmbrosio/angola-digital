from django.shortcuts import render, redirect
from .forms import ContatoForm

def home(request):
    return render(request, 'core/home.html')

def sobre(request):
    return render(request, 'core/sobre.html')

def servicos(request):
    return render(request, 'core/servicos.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:sucesso')
    else:
        form = ContatoForm()
    return render(request, 'core/contato.html', {'form': form})

def sucesso(request):
    return render(request, 'core/sucesso.html')
