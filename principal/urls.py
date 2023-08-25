from django.contrib import admin
from django.urls import path, include
# , usuarios, insumos, productos, proveedores, clientes, compras, login
from principal.views import inicio,login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('ventas/', include('ventas.urls')),
    path('usuarios/',include('usuarios.urls')),
    path('compras/',include('compras.urls')),
    path('login/', login, name='login'),
]
