from django.urls import path
from usuarios.views import usuarios, insumos, productos, servicios

urlpatterns = [
    path('usuarios/',usuarios,name="usuarios"),
    #pensé que se necesitaban los paths aquí lo dejo por si en algun momento es necesario
    path('insumos/',insumos, name="insumos"),
    path('productos/',productos, name="productos"),
    path('servicios/',servicios, name="servicios"),
]