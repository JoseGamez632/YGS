from django.contrib import admin
from django.urls import path, include
# from principal.views import inicial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ventas/',include('ventas.urls')),
    path('compras/',include('compras.urls')),
    path('usuarios/',include('usuarios.urls')),
    #path('index/',include('index.urls')),
]
