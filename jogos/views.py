from django.shortcuts import render

from .models import Modalidade, Equipe
# Create your views here.

def index(request):
    equipes = Equipe.objects.all()
    modalidade = Modalidade.objects.all()
    context = {
        "equipes": equipes,
        "modalidade": modalidade
    }
    return render (request, "index.html", context)

def modalidade(request):
    modalidade = Modalidade.objects.get(id=id)
    context = {
        "modalidade": modalidade
    }
    return render (request, "modalidade.html", context)

def equipe(request):
    equipe = Equipe.objects.get(id=id)
    context = {
        "equipe": equipe
    }
    return render (request, "equipe.html", context)