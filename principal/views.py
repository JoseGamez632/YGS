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

def insumos(request):
    titulo = "Insumos"
    context={
        'titulo':titulo
    }
    return render(request, "usuarios/insumos.html", context)

def servicios(request):
    titulo = "Servicios"
    context={
        'titulo':titulo
    }
    return render(request, "usuarios/servicios.html", context)

def productos(request):
    titulo = "Productos"
    context={
        'titulo':titulo
    }
    return render(request, "usuarios/productos.html", context)

def proveedores(request):
    titulo = "proveedores"
    context={
        'titulo':titulo
    }
    return render(request, "compras/proveedores.html", context)

def clientes(request):
    titulo = "Clientes"
    context={
        'titulo':titulo
    }
    return render(request, "ventas/Clientes.html", context)

def compras(request):
    titulo = "Insumos"
    context={
        'titulo':titulo
    }
    return render(request, "compras/compras.html", context)