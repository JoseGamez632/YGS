from django.db import models
from django.utils.translation import gettext_lazy as _
#from ventas.models import Venta

# Create your models here.
class Usuario(models.Model): #Falta cliente_id autoinclementable
    usu_id = models.AutoField(primary_key=True)
    usu_nombre_usuario = models.CharField(max_length=45, verbose_name="Nombre de Usuario")
    usu_nombre_apellido = models.CharField(max_length=45, verbose_name="Nombre y apellido")
    class tipoDoc(models.IntegerChoices):
        CC = 0, _('CC')
        CE = 1, _('CE')
        PEP = 2, _('PP')
    usu_tipo_documento = models.CharField(max_length=1, default=tipoDoc.CC, choices=tipoDoc.choices, verbose_name="Tipo documento")
    usu_num_documento = models.IntegerField(max_length=25, verbose_name="Numero de documento")
    usu_telefono = models.CharField(max_length=45, verbose_name="Telefono de usuario")
    usu_direccion = models.CharField(max_length=45, verbose_name="Dirección de usuario")
    usu_correo_electronico = models.CharField(max_length=45, verbose_name="Correo electronico de usuario")
    usu_clave = models.CharField(max_length=30, verbose_name="Contrasenia de acceso")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    usu_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    def __str__(self):
        return "%s %s" %(self.usu_nombre_apellido)
    
class Servicio(models.Model):
    serv_id = models.AutoField(primary_key=True)
    serv_nombre = models.CharField(max_length=45, verbose_name="Nombre de servicio")
    serv_descripcion = models.CharField(max_length=260, verbose_name="Descripción del servicio")
    serv_precio = models.IntegerField(verbose_name="Precio del servicio")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    serv_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    Usuario_usu_id = models.ForeignKey(Usuario, verbose_name="Id Usuario", on_delete=models.CASCADE)
    
class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True)
    prod_nombre = models.CharField(max_length=45, verbose_name= "Nombre del producto")
    prod_costo_prod = models.IntegerField(verbose_name= "Costo del producto")
    prod_precio_venta = models.IntegerField(verbose_name= "Precio de venta")
    stock = models.IntegerField(verbose_name="Stock")
    stock_min = models.IntegerField(verbose_name="Stock minimo")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    prod_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    Usuario_usu_id = models.ForeignKey(Usuario, verbose_name="Id Usuario")
    
class Insumos(models.Model):
    insumos_id = models.AutoField(primary_key=True)
    insum_nombre = models.CharField(max_length=45, verbose_name="Nombre del insumo")
    insum_precio = models.IntegerField(verbose_name="Precio del insumo")
    stock_min = models.IntegerField(verbose_name="Stock minimo de insumos")
    stock = models.IntegerField(verbose_name="Stock de insumos")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    insum_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    Usuario_usu_id = models.ForeignKey(Usuario,verbose_name="ID Usuario")