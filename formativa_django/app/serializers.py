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
        Fields = '__all__'

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