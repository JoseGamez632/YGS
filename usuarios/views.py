from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def usuarios(request):
    context={
    }
    return render(request,'usuarios/usuarios.html',context)
#pensé que podía ser necesario poner el def para cada  ventana aquí, lo dejo por si es necesario en algún momento
# def insumos(request):
#     context={
#     }
#     return render(request, "usuarios/insumos.html", context)

# def servicios(request):
#     context={
#     }
#     return render(request, "usuarios/servicios.html", context)

# def productos(request):
#     context={
#     }
#     return render(request, "usuarios/productos.html", context)