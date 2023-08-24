from django.urls import path
from usuarios.views import usuarios #insumos, productos, servicios

urlpatterns = [
    path('',usuarios,name="usuarios"),
    path('',usuarios,name="usuarios"),
    #pensé que se necesitaban los paths aquí lo dejo por si en algun momento es necesario
    # path('',insumos, name="insumos"),
    # path('',productos, name="productos"),
    # path('',servicios, name="servicios"),
]