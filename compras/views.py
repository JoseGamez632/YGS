from django.shortcuts import render

# Create your views here.

def compras(request):
    titulo = "Insumos"
    context={
        'titulo':titulo
    }
    return render(request, "compras/compras.html", context)

def proveedores(request):
    titulo = "Proveedores"
    context={
        'titulo': titulo
    }
    return render(request, 'compras/proveedores.html', context)