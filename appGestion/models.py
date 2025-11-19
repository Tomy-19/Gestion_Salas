from django.db import models
from django.utils import timezone
from datetime import timedelta

class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad_maxima = models.PositiveIntegerField()
    habilitada = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    @property
    def disponible(self):
        if not self.habilitada:
            return False

        reserva_activa = self.reservas.filter(
            fecha_termino__gte=timezone.now()
        ).exists()

        return not reserva_activa


class Reserva(models.Model):
    sala = models.ForeignKey(Sala, related_name='reservas', on_delete=models.CASCADE)
    rut = models.CharField(max_length=12)
    fecha_inicio = models.DateTimeField(editable=False)
    fecha_termino = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.fecha_inicio:
            self.fecha_inicio = timezone.now()

        max_fin = self.fecha_inicio + timedelta(hours=2)

        if not self.fecha_termino or self.fecha_termino > max_fin:
            self.fecha_termino = max_fin

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reserva {self.sala.nombre} - {self.rut}"
