from django.contrib import admin
from django.urls import path, include
from principal.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', inicio, name='inicio'),
    path('ventas/',include('ventas.urls')),
    path('compras/',include('compras.urls')),
    path('usuarios/',include('usuarios.urls')),
]
