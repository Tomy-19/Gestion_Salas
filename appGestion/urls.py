from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('salas/<int:pk>/', views.detalle_sala, name="detalle_sala"),
    path('salas/<int:pk>/reservar/', views.reservar_sala, name="reservar_sala"),
]