from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

telefone_validator = RegexValidator(
    regex=r'^\+?[\d\s\-\(\)]{10,20}$',
    message="Informe um número de telefone válido."
)
class Usuario(AbstractUser):
    TIPO_CHOICES = [
        ('G', 'Gestor'),
        ('P', 'Professor'),
    ]

    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, default='P')
    ni = models.PositiveIntegerField(unique=True)
    telefone = models.CharField(max_length=20, validators=[telefone_validator], help_text="Ex: +55 (47) 98888-7777")
    data_nascimento = models.DateField()
    data_contratacao = models.DateField()

    REQUIRED_FIELDS = ['ni', 'data_nascimento', 'data_contratacao']

    def __str__(self):
        return f'{self.username} ({self.get_tipo_display()})'

class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    curso = models.CharField(max_length=255)
    carga_hora = models.IntegerField()
    descricao = models.TextField(blank=True, null=True)
    professor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'tipo': 'P'})

    def __str__(self):
        return self.nome

class Sala(models.Model):
    nome = models.CharField(max_length=255)
    capacidade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

class ReservaAmbiente(models.Model):
    PERIODO = [
        ('MANHA', 'Manhã'),
        ('TARDE', 'Tarde'),
        ('NOITE', 'Noite',)
    ]
    data_inicio = models.DateField()
    data_termino = models.DateField()
    periodo = models.CharField(max_length=5, choices=PERIODO)
    sala_reservada = models.ForeignKey(Sala, on_delete=models.CASCADE)
    professor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'tipo': 'P'})
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sala_reservada} - {self.get_periodo_display()} {self. data_inicio} a {self.data_termino} '

