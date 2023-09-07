from django.urls import path
from ventas.views import ventas, clientes

urlpatterns = [
    path('ventas/',ventas,name="ventas"),
    path('clientes/',clientes,name="clientes"),
]
