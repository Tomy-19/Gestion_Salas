from django.contrib import admin
from .models import Sala, Reserva

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "capacidad_maxima", "habilitada")
    list_filter = ("habilitada",)
    search_fields = ("nombre",)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("sala", "rut", "fecha_inicio", "fecha_termino")
    list_filter = ("sala",)
    search_fields = ("rut", "sala__nombre")
