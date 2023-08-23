from django.shortcuts import render

def inicio(request):
    titulo = "Inicio"
    context={
        'titulo':titulo
    }
    return render(request, "index.html", context)

def ventas(request):
    titulo = "Ventas"
    context={
        'titulo':titulo
    }
    return render(request, "ventas/ventas.html", context)


def usuarios(request):
    titulo = "Usuarios"
    context={
        'titulo':titulo
    }
    return render(request, "usuarios/usuarios.html", context)