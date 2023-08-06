from django.db import models
from django.utils.translation import gettext_lazy as _
#from ventas.models import Venta

# Create your models here.
"""class Usuario(models.Model): #Falta cliente_id autoinclementable
    usu_nombre = models.CharField(max_length=45, verbose_name="Nombre usuario")
    usu_apellido = models.CharField(max_length=45, verbose_name="Apellido usuario")
    usu_num_documento = models.CharField(max_length=15, verbose_name="Número de documento")
    usu_telefono = models.CharField(max_length=15, verbose_name="Número de teléfono")
    usu_direccion = models.CharField(max_length=15, verbose_name="Dirección del usuario")
    usu_correo_electronico = models.CharField(max_length=15, verbose_name="Email del usuario")
    usu_clave = models.CharField(max_length=15, verbose_name="clave del usuario")
    class TipoDoc(models.IntegerChoices):
        CC = 0, _('CC')
        CE = 1, _('CE')
        PEP = 2, _('PEP')
        PA = 3, _('PA')
        NIT = 4, _('NIT')
        OT = 5, _('OTRO')
    usu_tipo_documento = models.IntegerField(default=TipoDoc.CC, choices=TipoDoc.choices, verbose_name="Tipo documento")
    usu_num_documento = models.CharField(max_length=25, verbose_name="Numero de documento")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    def __str__(self):
        return "%s %s" %(self.usu_nombre, self.usu_apellido)
    
class Servicios(models.Model):
    usuario_usu_id = models.ForeignKey(Usuario, verbose_name="Usuario", on_delete=models.PROTECT, related_name='Usuario')
    #venta_vent_id = models.ForeignKey(Venta, on_delete=models.PROTECT, verbose_name="Número de venta")
    serv_nombre = models.CharField(max_length=45, verbose_name="Nombre del servicio")
    serv_codigo = models.CharField(max_length=45, verbose_name="Código del servicio")
    serv_descripcion = models.CharField(max_length=45, verbose_name="Descripción del servicio")
    serv_categoria = models.CharField(max_length=45, verbose_name="Categoría del servicio")
    serv_pago_total = models.IntegerField(verbose_name="Pago total")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    
class Productos(models.Model):
    usuario_usu_id = models.ForeignKey(Usuario, verbose_name="Usuario", on_delete=models.PROTECT, related_name='Usuario')
    #venta_vent_id = models.ForeignKey(Venta, on_delete=models.PROTECT, verbose_name="Número de venta")
    prod_nombre = models.CharField(max_length=45, verbose_name="Nombre del producto")
    prod_codigo = models.CharField(max_length=45, verbose_name="Código del producto")
    prod_descripcion = models.CharField(max_length=45, verbose_name="Descripción del producto")
    prod_precio_compra = models.IntegerField(max_length=45, verbose_name="Precio de compra")
    prod_precio_venta = models.IntegerField(max_length=45, verbose_name="Precio de venta")
    Stock_min = models.IntegerField(max_length=45, verbose_name="Mínimo inventario")
    Stock = models.IntegerField(max_length=45, verbose_name="Inventario")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

class Insumos(models.Model):
    usuario_usu_id = models.ForeignKey(Usuario, verbose_name="Usuario", on_delete=models.PROTECT, related_name='Usuario')
    insum_nombre = models.CharField(max_length=45, verbose_name="Nombre del insumo")
    insum_categoria = models.CharField(max_length=45, verbose_name="Categoría del insumo")
    insum_codigo = models.CharField(max_length=45, verbose_name="Código del insumo")
    insum_cantidad = models.IntegerField(max_length=45, verbose_name="Cantidad de insumo")
    insum_precio_compra = models.IntegerField(max_length=45, verbose_name="Precio de compra")
    insum_total = models.IntegerField(max_length=45, verbose_name="Precio de venta")
    Stock_min = models.IntegerField(max_length=45, verbose_name="Mínimo inventario")
    Stock = models.IntegerField(max_length=45, verbose_name="Inventario")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
  """