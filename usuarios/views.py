from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def usuarios(request):
    titulo = "Usuarios"
    context={
        'titulo':titulo
    }
    return render(request, "usuarios/usuarios.html", context)

def insumos(request):
    titulo = "Insumos"
    context={
        'titulo':titulo
    }
    return render(request, "usuarios/insumos.html", context)

def productos(request):
    titulo = "Productos"
    context={
        'titulo':titulo
    }
    return render(request, "usuarios/productos.html", context)

def servicios(request):
    titulo = "Servicios"
    context={
        'titulo':titulo
    }
    return render(request, "usuarios/servicios.html", context)