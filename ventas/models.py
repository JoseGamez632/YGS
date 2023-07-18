from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Cliente(models.Model): #Falta cliente_id autoinclementable
    clie_nombre = models.CharField(max_length=45, verbose_name="Nombre Cliente")
    clie_apellido = models.CharField(max_length=45, verbose_name="Apellido Cliente")
    clie_telefono = models.CharField(max_length=45, verbose_name="Teléfono Cliente")
    clie_direccion = models.CharField(max_length=45, verbose_name="Dirección Cliente")
    class TipoDoc(models.IntegerChoices):
        CC = 0, _('Cédula ciudadanía')
        CE = 1, _('Tarjeta de identidad extranjera')
        PA = 2, _('Pasaporte')
        NIT = 3, _('Numero de identificación tributaria')
        OT = 4, _('Otro tipo de documento')
    clie_tipo_documento = models.IntegerField(default=TipoDoc.CE, choices=TipoDoc.choices, verbose_name="Tipo documento")
    clie_num_documento = models.IntegerField(verbose_name="Numero de documento")
    clie_correo_electronico = models.CharField(max_length=45, verbose_name="Correo cliente")
    def __str__(self):
        return "%s %s" %(self.clie_nombre, self.clie_apellido)
    
class Detalle_Venta(models.Model): #Falta venta_has_clientecol y venta_vent_id "autoincrementable"
    det_vent_precio_unitario = models.IntegerField(verbose_name="Precio unitario de producto")
    det_vent_cantidad = models.IntegerField(verbose_name="Cantidad producto")
    det_vent_precio_total = models.IntegerField(verbose_name="Precio total")

class Venta(models.Model):
    vent_fecha = models.DateField(verbose_name="Fecha de venta")
    vent_cliente = models.CharField(max_length=45, verbose_name="Nombre de cliente")
    vent_precio_subtotal = models.IntegerField(verbose_name="Precio subtotal")
    vent_iva = models.IntegerField(verbose_name="IVA")
    vent_precio_total = models.IntegerField(verbose_name="Precio total")