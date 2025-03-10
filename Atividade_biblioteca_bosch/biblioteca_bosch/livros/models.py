from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    ano_publicacao = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.titulo