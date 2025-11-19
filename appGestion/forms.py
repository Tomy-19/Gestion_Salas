from django import forms
from .models import Reserva

class ReservaSalaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ("rut",)