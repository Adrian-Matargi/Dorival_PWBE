from django.db import models

class Piloto(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.PositiveIntegerField()
    classificacao = models.PositiveIntegerField()
    equipe = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nome} esta na {self.classificacao} posição'

class Carro(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    velocidade_maxima = models.PositiveIntegerField()
    escolha_cores = (
        ('VERMELHO', 'Vermelho'),
        ('ROSA', 'Rosa'),
        ('BRANCO', 'Branco'),
        ('PRETO', 'Preto'),
        ('VERDE', 'Verde'),
        ('MARROM', 'Marrom'),
        ('ROXO', 'Roxo'),
        ('CINZA', 'Cinza'),
        ('DOURADO', 'Dourado')
    )
    cor = models.CharField(max_length=50, choices=escolha_cores)
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)