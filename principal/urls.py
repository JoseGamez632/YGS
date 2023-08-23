from django.contrib import admin
from django.urls import path, include
from principal.views import inicio, ventas, usuarios

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', inicio, name='inicio'),
    path('ventas/', ventas, name='ventas'),
    path('usuarios/',usuarios, name='usuarios'),
]
