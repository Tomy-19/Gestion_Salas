from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Sala
from .forms import ReservaSalaForm

def main(request):
    salas = Sala.objects.all().order_by("nombre")
    return render(request, "salas/lista_salas.html", {"salas": salas})

def detalle_sala(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    reserva_activa = sala.reservas.filter(
        fecha_termino__gte=timezone.now()
    ).order_by("-fecha_inicio").first()
    context = {
        "sala": sala,
        "reserva_activa": reserva_activa,
    }
    return render(request, "salas/detalle_sala.html", context)

def reservar_sala(request, pk):
    sala = get_object_or_404(Sala, pk=pk)

    if not sala.disponible:
        return redirect("detalle_sala", pk=sala.pk)

    if request.method == "POST":
        form = ReservaSalaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.sala = sala
            reserva.save()
            return redirect("detalle_sala", pk=sala.pk)
    else:
        form = ReservaSalaForm()

    return render(request, "reservas/nueva_reserva.html", {"sala": sala, "form": form})
