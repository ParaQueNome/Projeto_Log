from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
# Criando os modelos sql

class Projeto_Log(models.Model):
    nome_feriado = models.CharField("Feriado", _MAX_LENGTH=50)
    dia = models.IntegerField('Dia')
    mes = models.IntegerField("Mês")
    modificado_em = models.DateTimeField(
    verbose_name='modificado em',
    auto_now_add=False, auto_now=True)

def __str__(self):
    return self.nome