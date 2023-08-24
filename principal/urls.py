from django.contrib import admin
from django.urls import path, include
from principal.views import inicio, ventas, usuarios, insumos, productos, servicios, proveedores, clientes

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', inicio, name='inicio'),
    path('ventas/', ventas, name='ventas'),
    path('usuarios/',usuarios, name='usuarios'),
    path('insumos/',insumos, name='insumos'),
    path('productos/',productos, name='productos'),
    path('servicios/',servicios, name='servicios'),
    path('proveedores/',proveedores, name='proveedores'),
    path('clientes/',clientes, name='clientes'),
]
