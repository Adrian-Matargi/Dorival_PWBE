from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Piloto, Carro
from .serializers import PilotoSerializer, CarroSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class PilotoPaginacao(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

class PilotoRetrieveUpdateDestroyAPIview(RetrieveUpdateDestroyAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    lookup_field = 'pk'

    @swagger_auto_schema(
        operation_description='Pega o piloto do ID fornecido',
        responses={
            200: PilotoSerializer,
            404: 'Not Found',
            400: 'Error'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class PilotoListCreateAPIView(ListCreateAPIView):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    pagination_class = PilotoPaginacao

    @swagger_auto_schema(
            operation_description='Lista todos os pilotos de Formula 1',
            responses={
                200: PilotoSerializer(many=True),
                400: 'Error'
            },
            manual_parameters=[
                openapi.Parameter(
                    'nome',
                    openapi.IN_QUERY,
                    description='Filtrar pelo nome do piloto',
                    type=openapi.TYPE_STRING
                )
            ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
            operation_description='Cria um novo Piloto',
            request_body=PilotoSerializer,
            responses={
                201: PilotoSerializer,
                400: 'Error'
            }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset
    
    def perform_create(self, serializer):
        if serializer.validated_data['equipe'] != 'DS16' and serializer.validated_data['classificacao'] <= 5:
            return serializers.ValidationError('Somente a DS16 deve ficar entre os 5')
        serializer.save()
        

class CarroPaginacao(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

class CarroRetrieveUpdateDestroyAPIview(RetrieveUpdateDestroyAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    lookup_field = 'pk'

    @swagger_auto_schema(
        operation_description='Pega o carro pelo ID fornecido',
        responses={
            200: CarroSerializer,
            404: 'Not Found',
            400: 'Error'
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class CarroListCreateAPIView(ListCreateAPIView):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    pagination_class = CarroPaginacao

    @swagger_auto_schema(
        operation_description='Lista todos os carros',
        responses={
            200: CarroSerializer(many=True),
            400: 'Error'
        },
        manual_parameters=[
            openapi.Parameter(
                'marca',
                openapi.IN_QUERY,
                description='Filtrar pela marca do carro',
                type=openapi.TYPE_STRING
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Cria um novo Carro',
        request_body=CarroSerializer,
        responses={
            201: CarroSerializer,
            400: 'Error'
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        marca = self.request.query_params.get('marca')
        if marca:
            queryset = queryset.filter(marca__icontains=marca)
        return queryset