from rest_framework import serializers
from .models import UsuarioDS16

class UsuarioDS16Serializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioDS16
        fields = [
            'id',
            'username',
            'email',
            'biografia',
            'idade',
            'telefone',
            'endereco',
            'escolaridade',
            'animais',
            'is_active',
            'is_staff',
            'is_superuser',
            'date_joined',
            'last_login',
        ]
        read_only_fields = ['id', 'is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login']
