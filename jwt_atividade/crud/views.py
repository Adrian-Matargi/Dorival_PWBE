from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def criar_usuario(request):
    username = request.data.get('username')
    senha = request.data.get('senha')
    biografia = request.data.get('biografia')
    idade = request.data.get('idade')
    telefone = request.data.get('telefone')
    enderoco = request.data.get('endereco')
    escolaridade = request.data.get('escolaridade')
    animais = request.data.get('animais')

    if not username or not senha or not idade or not telefone or not escolaridade:
        return Response({'Erro':'Campos obrigatórios incompletos'})