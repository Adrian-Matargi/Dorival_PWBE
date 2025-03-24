from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=255, null=True, blank=True)
    categoria = models.CharField(max_length=255, null=True, blank=True)