from django.urls import path
from .views import PilotoListCreateAPIView, PilotoRetrieveUpdateDestroyAPIview

urlpatterns = [
    path('piloto/', view=PilotoListCreateAPIView.as_view()),
    path('piloto/<int:pk>/', view=PilotoRetrieveUpdateDestroyAPIview.as_view()),
]
