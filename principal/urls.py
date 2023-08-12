from django.contrib import admin
from django.urls import path, include
from principal.views import hola_mundo, indexAugusto,   indexAugusto2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hola_mundo, name='inicio'),
    path('ventas/',include('ventas.urls')),
    path('compras/',include('compras.urls')),
    path('usuarios/',include('usuarios.urls')),
    path('indexAugusto/', indexAugusto, name='indexAugusto'),
    path('indexAugusto2/', indexAugusto2, name='indexAugusto2'),

]

