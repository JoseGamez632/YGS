from django.db import models
from django.utils.translation import gettext_lazy as _
#from ventas.models import Venta

# Create your models here.
class Usuario(models.Model): #Falta cliente_id autoinclementable
    usu_id = models.AutoField(primary_key=True, default=None)
    usu_nombre_usuario = models.CharField(max_length=45, verbose_name="Nombre de Usuario", default=None)
    usu_nombre_apellido = models.CharField(max_length=45, verbose_name="Nombre y apellido", default=None)
    class tipoDoc(models.IntegerChoices):
        CC = 0, _('CC')
        CE = 1, _('CE')
        PEP = 2, _('PP')
    usu_tipo_documento = models.CharField(max_length=1, default=tipoDoc.CC, choices=tipoDoc.choices, verbose_name="Tipo documento")
    usu_num_documento = models.IntegerField(verbose_name="Numero de documento", default=None)
    usu_telefono = models.CharField(max_length=45, verbose_name="Telefono de usuario", default=None)
    usu_direccion = models.CharField(max_length=45, verbose_name="Dirección de usuario", default=None)
    usu_correo_electronico = models.CharField(max_length=45, verbose_name="Correo electronico de usuario", default=None)
    usu_clave = models.CharField(max_length=30, verbose_name="Contrasenia de acceso", default=None)
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    usu_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    def __str__(self):
        return "%s %s" %(self.usu_nombre_apellido)
    
class Servicio(models.Model):
    serv_id = models.AutoField(primary_key=True, default=None)
    serv_nombre = models.CharField(max_length=45, verbose_name="Nombre de servicio", default=None)
    serv_descripcion = models.CharField(max_length=260, verbose_name="Descripción del servicio", default=None)
    serv_precio = models.IntegerField(verbose_name="Precio del servicio", default=None)
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    serv_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    Usuario_usu_id = models.ForeignKey(Usuario, verbose_name="Id Usuario", on_delete=models.CASCADE, default=None)
    
class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True, default=None)
    prod_nombre = models.CharField(max_length=45, verbose_name= "Nombre del producto", default=None)
    prod_costo_prod = models.IntegerField(verbose_name= "Costo del producto", default=None)
    prod_precio_venta = models.IntegerField(verbose_name= "Precio de venta", default=None)
    stock = models.IntegerField(verbose_name="Stock", default=None)
    stock_min = models.IntegerField(verbose_name="Stock minimo", default=None)
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    prod_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    Usuario_usu_id = models.ForeignKey(Usuario, verbose_name="Id Usuario", on_delete=models.CASCADE, default=None)
    
class Insumo(models.Model):
    insumos_id = models.AutoField(primary_key=True, default=None)
    insum_nombre = models.CharField(max_length=45, verbose_name="Nombre del insumo", default=None)
    insum_precio = models.IntegerField(verbose_name="Precio del insumo", default=None)
    stock_min = models.IntegerField(verbose_name="Stock minimo de insumos", default=None)
    stock = models.IntegerField(verbose_name="Stock de insumos", default=None)
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    insum_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    Usuario_usu_id = models.ForeignKey(Usuario,verbose_name="ID Usuario", on_delete=models.CASCADE, default=None)