from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import UsuarioDS16
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import UsuarioDS16Serializer

@api_view(['POST'])
def criar_usuario(request):
    username = request.data.get('username')
    senha = request.data.get('senha')
    biografia = request.data.get('biografia')
    idade = request.data.get('idade')
    telefone = request.data.get('telefone')
    endereco = request.data.get('endereco')
    escolaridade = request.data.get('escolaridade')
    animais = request.data.get('animais')

    if not username or not senha or not idade or not telefone or not escolaridade:
        return Response({'Erro':'Campos obrigatorios incompletos'}, status=status.HTTP_400_BAD_REQUEST)
    
    if UsuarioDS16.objects.filter(username=username).exists():
        return Response({'Erro': f'Username {username} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    
    usuario = UsuarioDS16.objects.create_user(
        username=username,
        password=senha,
        biografia=biografia,
        idade=idade,
        telefone=telefone,
        endereco=endereco,
        escolaridade=escolaridade,
        animais=animais,
        email=f"{username}@ds16.com"
    )
    return Response({'Mensagem': f'Usuario {username} criado com sucesso'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logar_usuario(request):
    username = request.data.get('username')
    senha = request.data.get('senha')

    usuario = authenticate(username=username, password=senha)

    if usuario:
        refresh = RefreshToken.for_user(usuario)
        
        return Response({
            'acesso': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_200_OK)
    else:
        return Response({'Erro': 'Usuario ou/e senha incorreto(s)'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read(request):
    usuarios = UsuarioDS16.objects.all()
    serializer = UsuarioDS16Serializer(usuarios, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_usuario(request, pk):
    try:
        usuario = UsuarioDS16.objects.get(pk=pk)
    except UsuarioDS16.DoesNotExist:
        return Response({'erro': 'Usuário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UsuarioDS16Serializer(usuario, data=request.data, partial=True)  # partial=True permite PATCH
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_usuario(request, pk):
    try:
        usuario = UsuarioDS16.objects.get(pk=pk)
    except UsuarioDS16.DoesNotExist:
        return Response({'erro': 'Usuário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    usuario.delete()
    return Response({'mensagem': 'Usuário deletado com sucesso.'}, status=status.HTTP_204_NO_CONTENT)
