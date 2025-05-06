from django.urls import path
from .views import LoginView, UsuarioListCreate, UsuarioRtriveveUpdateDestroy, ReservaAmbienteListCreate, ReservaAmbienteRetriveUpdateDestroy, ReservaAmbienteProfessorList, DisciplinaListCreate, DisciplinaRetriverUpdateDestroy, DisciplinaProfessorList, SalaListCreate, SalaRetriveUpdateDestroy

urlpatterns = [
    path('login/', LoginView.as_view()),
    
    path('usuario/', UsuarioListCreate.as_view()),
    path('usuario/<int:pk>/', UsuarioRtriveveUpdateDestroy.as_view()),
    
    path('reservas/', ReservaAmbienteListCreate.as_view()),
    path('reserva/<int:pk>/', ReservaAmbienteRetriveUpdateDestroy.as_view()),
    path('professor/reservas/', ReservaAmbienteProfessorList.as_view()),

    path('disciplinas/', DisciplinaListCreate.as_view()),
    path('disciplinas/<int:pk>/', DisciplinaRetriverUpdateDestroy.as_view()),
    path('professor/disciplinas/', DisciplinaProfessorList.as_view()),

    path('salas/', SalaListCreate.as_view()),
    path('salas/<int:pk>', SalaRetriveUpdateDestroy.as_view())

]
