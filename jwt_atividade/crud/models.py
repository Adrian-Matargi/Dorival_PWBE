from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    biografia = models.TextField(null=True, balnk=True)
    idade = models.PositiveIntegerField()
    telefone = models.CharField()
    endereco = models.TextField()
    escolaridade = models.CharField(max_length=255)
    animais = models.PositiveIntegerField()
    REQUIRED_FIELDS = ['idade', 'telefone', 'escolaridade']

    def __str__(self):
        return self.username