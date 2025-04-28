from django.urls import path
from .views import PilotoListCreateAPIView, PilotoRetrieveUpdateDestroyAPIview, CarroRetrieveUpdateDestroyAPIview, CarroListCreateAPIView

urlpatterns = [
    path('piloto/', view=PilotoListCreateAPIView.as_view()),
    path('piloto/<int:pk>/', view=PilotoRetrieveUpdateDestroyAPIview.as_view()),
    path('carros/', CarroListCreateAPIView.as_view()),
    path('carros/<int:pk>/', CarroRetrieveUpdateDestroyAPIview.as_view()),
]
