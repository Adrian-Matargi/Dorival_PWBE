from django.urls import path
from . import views

urlpatterns = [
    path('criar/', view=views.criar_usuario, name='criar_usuario'),
    path('logar/', view=views.logar_usuario, name='logar_usuario'),
    path('read/', view=views.read, name='read'),
    path('update/<int:pk>/', view=views.update_usuario, name='update_usuario'),
    path('delete/<int:pk>/', view=views.delete_usuario, name='delete_usuario' ),
]
