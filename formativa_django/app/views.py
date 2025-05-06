from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Usuario, Disciplina, ReservaAmbiente, Sala
from .serializers import UsuarioSerializer, DisciplinaSerializer, ReservaAmbienteSerializer, LoginSerializer, SalaSerializer
from .permissions import IsGestor, IsProfessor, IsDonoOuGestor
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

class UsuarioListCreate(ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsGestor]

class UsuarioRtriveveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer = UsuarioSerializer
    permission_classs = [IsGestor]
    lookup_field = 'pk'

class DisciplinaListCreate(ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]
    
class DisciplinaRetriverUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [IsGestor]
    lookup_field = 'pk'

class DisciplinaProfessorList(ListAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = [IsProfessor]

    def get_queryset(self):
        return Disciplina.objects.filter(professor=self.request.user)
    
class ReservaAmbienteListCreate(ListCreateAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]

    def get_queryset(self):
        queryset = super().get_queryset()
        professor_id = self.request.query_params.get('professor', None)
        if professor_id:
            queryset = queryset.filter(professor_id=professor_id)
        return queryset
    
class ReservaAmbienteRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer
    permission_classes = [IsDonoOuGestor]
    lookup_field = 'pk'

class ReservaAmbienteProfessorList(ListAPIView):
    serializer_class = ReservaAmbienteSerializer
    permission_classes = [IsProfessor]

    def get_queryset(self):
        return ReservaAmbiente.objects.filter(professor=self.request.user)
    
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class SalaListCreate(ListCreateAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsGestor()]
    
class SalaRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    permission_class = [IsGestor]
    lookup_field = 'pk'

class SalaProfessorList(ListAPIView):
    serializer_class = SalaSerializer
    permission_classes = [IsProfessor]

    def get_queryset(self):
        return Sala.objects.filter(professor=self.request.user)