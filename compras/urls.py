from django.urls import path
from compras.views import compras, proveedores

urlpatterns = [
    path('compras/',compras,name="compras"),
    path('proveedores/', proveedores, name="proveedores"),
]