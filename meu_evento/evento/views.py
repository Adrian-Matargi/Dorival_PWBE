from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Evento
from .serializers import EventoSerializer
from django.utils import timezone
from datetime import timedelta

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria = self.request.query_params.get('categoria')
        data = self.request.query_params.get('data')
        quantidade = self.request.query_params.get('quantidade')
        ordering = self.request.query_params.get('ordering')

        if categoria:
            queryset = queryset.filter(categoria=categoria)

        if data:
            queryset = queryset.filter(data_hora__date=data)

        if quantidade:
            queryset = queryset[:int(quantidade)]
        
        if ordering:
            queryset = queryset.order_by(ordering)
        
        return queryset
    
    @action(detail=False)
    def proximos(self, request):
        agora = timezone.now()
        futuro = agora + timedelta(days=7)
        eventos = Evento.objects.filter(data_hora__gte=agora, data_hora__lte=futuro)
        serializer = self.get_serializer(eventos, many=True)
        return Response(serializer.data)