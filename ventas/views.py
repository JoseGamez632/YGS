from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def ventas(request):
    titulo = "Ventas"
    context={
        'titulo':titulo
    }
    return render(request, "ventas/ventas.html", context)

def clientes(request):
    titulo = "Clientes"
    context={
        'titulo':titulo
    }
    return render(request, "ventas/Clientes.html", context)