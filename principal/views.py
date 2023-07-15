from django.shortcuts import render


def hola_mundo(request):
    nombre = "Jose",
    apellido = "Gamez",
    telefono = "83892394"

    context={
        'nombres':nombre,
        'apellidos':apellido,
        'telefonos':telefono

    }
    return render(request, "index.html", context)