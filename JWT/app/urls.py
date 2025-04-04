from django.urls import path
from . import views

urlpatterns = [
    path('criar/', view=views.criar_usuario, name='criar_usuario'),
    path('logar/', view=views.logar_usuario, name='logar_usuario'),
    path('read/', view=views.read, name='read'),
]
