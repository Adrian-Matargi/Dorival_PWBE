from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'

class ReservaAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaAmbiente
        fields = '__all__'
    
    def validate(self, data):
        sala_reservada = data.get('sala_reservada')
        professor = data.get('professor')
        data_inicio = data.get('data_inicio')
        data_termino = data.get('data_termino')
        periodo = data.get('periodo')

        reservas_conflito = ReservaAmbiente.objects.filter(
            sala_reservada=sala_reservada,
            periodo=periodo,
            professor=professor
        ).filter(
            data_inicio__lt=data_termino,
            data_termino__gt=data_inicio
        )

        if reservas_conflito.exists():
            raise serializers.ValidationError("Já existe uma reserva conflitante para este professor nesta sala e período.")

        if data_termino <= data_inicio:
            raise serializers.ValidationError("A data de término deve ser posterior à de início.")
        
        return data

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    
class LoginSerializer(TokenObtainPairSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        data = super().validate(attrs)

        data['user'] = {
            'username': self.user.username,
            'email': self.user.email,
            'tipo': self.user.tipo
        }
        return data