from django.db import models
from django.core.validators import RegexValidator

telefone_validator = RegexValidator(
    regex=r'^\+?[\d\s\-\(\)]{10,20}$',
    message="Informe um número de telefone válido."
)

class Professor(models.Model):
    ni = models.PositiveIntegerField()
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, validators=[telefone_validator], help_text="Ex: +55 (47) 98888-7777")
    data_nascimento = models.DateField()
    data_contracao = models.DateField()

class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)
    carga_hora = models.IntegerField()
    descricao = models.TextField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='disciplinas')

class Sala(models.Model):
    nome = models.CharField(max_length=255)
    capacidade = models.PositiveIntegerField()

class ReservaAmbiente(models.Model):
    PERIODO = [
        ('MANHA', 'Manhã'),
        ('TARDE', 'Tarde'),
        ('NOITE', 'Noite',)
    ]
    data_inicio = models.DateField()
    data_termino = models.DateField()
    periodo = models.CharField(max_length=10, choices=PERIODO)
    sala_reservada = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='sala')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='reserva_ambiente')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='disciplina')