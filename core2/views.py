from asyncore import dispatcher_with_send
from django.shortcuts import render
from datetime import datetime
from .models import Projeto_Log

# Create your views here.
def verifica_feriado(request):
    hoje = datetime.today()
    resultado = Projeto_Log.objects.filter(dia=hoje.day).filter(mes=hoje.month)
    if len(resultado) > 0:
        contexto = {'feriado': True, 'nome': resultado[0].nome}
    else:
        contexto = {'feriado': False}
    return render(request, 'feriados.html', contexto)