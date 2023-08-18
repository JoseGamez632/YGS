from django.shortcuts import render

def inicio(request):
    nombre = "Jose"
    apellido = "Gamez"
    telefono = "83892394"

    context={
        'nombres':nombre,
        'apellidos':apellido,
        'telefonos':telefono

    }
    return render(request, "index.html", context)

def ventas(request):
    context={
    }
    return render(request, "ventas.html", context)


def usuarios(request):
    context={
    }
    return render(request, "usuarios.html", context)