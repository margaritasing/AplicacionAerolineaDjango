from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from .models import Vuelo, Pasajero
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

# Create your views here.

def index(request):
    return render(request,"vuelos/index.html", {
        "lista_vuelos": Vuelo.objects.all()
    })

@permission_required('AEROLINEA.view_vuelo')
def vuelo(request, vuelo_id):
    vuelo = Vuelo.objects.get(id=vuelo_id)
    pasajeros = vuelo.pasajeros.all()
    no_son_pasajeros = Pasajero.objects.exclude(vuelos=vuelo).all()
    return render(request, "vuelos/vuelo.html", {
        "vuelo": vuelo,
        "pasajeros": pasajeros,
        "no_son_pasajeros": no_son_pasajeros
    })

@permission_required('AEROLINEA.add_vuelo')
def vuelo_alta(request):
    #VueloForm = modelform_factory(Vuelo, fields=("origen", "destino", "duracion"))
    if request.method == "POST":
        form = FormVueloCustom(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormVueloCustom()
        return render(request, "vuelos/vuelo_alta.html", {
            "formset": form
        })

@permission_required('AEROLINEA.change_vuelo')
def vuelo_modificar(request, vuelo_id):
    un_vuelo = get_object_or_404(Vuelo, id=vuelo_id)
    
    if request.method == "POST":     
        form = FormVueloCustom(request.POST, instance = un_vuelo) 
        if form.is_valid():
            form.save()
            return render(request,"vuelos/index.html", {
                "lista_vuelos": Vuelo.objects.all()
            })
    else:
        form = FormVueloCustom(instance = un_vuelo)
        return render(request, 'vuelos/vuelo_modificar.html', {
            "un_vuelo": un_vuelo,
            "form": form
        })

@permission_required('AEROLINEA.delete_vuelo')
def vuelo_eliminar(request, vuelo_id):
    un_vuelo = get_object_or_404(Vuelo, id=vuelo_id)
    un_vuelo.delete()
    return render(request,"vuelos/index.html", {
        "lista_vuelos": Vuelo.objects.all()
    })

@login_required
def reserva(request, vuelo_id):
    if request.method == "POST":
        vuelo = Vuelo.objects.get(pk=vuelo_id)
        pasajero_id = int(request.POST["pasajero"])
        pasajero = Pasajero.objects.get(pk=pasajero_id)
        pasajero.vuelos.add(vuelo)
        return HttpResponseRedirect(reverse("AEROLINEA:vuelo", args=(vuelo.id,)))

