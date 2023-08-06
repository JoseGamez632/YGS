from django.db import models
from django.utils.translation import gettext_lazy as _
#from usuarios.models import Usuario

# Create your models here.
class Cliente(models.Model): #Falta cliente_id autoinclementable
    clie_nombre = models.CharField(max_length=45, verbose_name="Nombre Cliente")
    clie_apellido = models.CharField(max_length=45, verbose_name="Apellido Cliente")
    clie_telefono = models.CharField(max_length=15, verbose_name="Teléfono Cliente")
    clie_direccion = models.CharField(max_length=45, verbose_name="Dirección Cliente")
    class TipoDoc(models.IntegerChoices):
        CC = 0, _('CC')
        CE = 1, _('CE')
        PEP = 2, _('PEP')
        PA = 3, _('PA')
        NIT = 4, _('NIT')
        OT = 5, _('OTRO')
    clie_tipo_documento = models.IntegerField(default=TipoDoc.CC, choices=TipoDoc.choices, verbose_name="Tipo documento")
    clie_num_documento = models.CharField(max_length=25, verbose_name="Numero de documento")
    clie_correo_electronico = models.CharField(max_length=45, verbose_name="Correo cliente")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    def __str__(self):
        return "%s %s" %(self.clie_nombre, self.clie_apellido)
    
class Venta(models.Model):
    usuario_usu_id = models.ForeignKey(Usuario, verbose_name="Usuario", on_delete=models.PROTECT, related_name='Usuario')
    vent_fecha = models.DateField(verbose_name="Fecha de venta")
    vent_precio_subtotal = models.IntegerField(verbose_name="Precio subtotal")
    vent_iva = models.IntegerField(verbose_name="IVA")
    vent_precio_total = models.IntegerField(verbose_name="Precio total")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    
class Detalle_Venta(models.Model): #Falta venta_has_clientecol y venta_vent_id "autoincrementable"
    venta_vent_id = models.ForeignKey(Venta, on_delete=models.PROTECT, verbose_name="Número de venta")
    cliente_clie_id = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name="Número de cliente")
    det_vent_precio_unitario = models.IntegerField(verbose_name="Precio unitario de producto")
    det_vent_cantidad = models.IntegerField(verbose_name="Cantidad producto")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")