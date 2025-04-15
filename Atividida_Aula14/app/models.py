from django.db import models
from django.contrib.auth.models import AbstractUser

class UsuarioDS16(AbstractUser):
    biografia = models.TextField()
    idade = models.PositiveIntegerField()
    telefone = models.CharField(max_length=255)
    endereco = models.TextField()
    escolaridade = models.CharField(max_length=255)
    animais = models.CharField(max_length=255, blank=True, null=True)
    REQUIRED_FIELDS = ['idade', 'telefone', 'escolaridade']

    def __str__(self):
        return self.username