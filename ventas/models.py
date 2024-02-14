from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import Usuario, Servicio, Producto

# Create your models here.
class Cliente(models.Model): #Falta cliente_id autoinclementable
    clie_id = models.AutoField(primary_key=True, default=None) 
    clie_nombre = models.CharField(max_length=45, verbose_name='Nombre cliente', default=None)
    clie_apellido = models.CharField(max_length=45, verbose_name="Apellido proveedor", default=None)
    clie_telefono = models.CharField(max_length=45, verbose_name="Telefono Cliente", default=None)
    class tipoDoc (models.IntegerChoices):
        CC = 0, _( "Cedula de Ciudadania")
        CE = 1, _( "Cedula de Extranjeria")
        PEP = 2, _( "Permiso de permanencia")
        PA = 3, _( "Pasaporte")
        NIT = 4, _( "Numero Identificacion Tributaria")
        OTRO = 5, _( "Otro")
    clie_tipo_documento = models.CharField(max_length=1, choices=tipoDoc.choices, default=tipoDoc.CC, verbose_name="Tipo de documento del cliente")
    clie_num_documento = models.CharField(max_length=16, verbose_name="Numero documento cliente", default=None)
    clie_correo_electronico = models.CharField(max_length=45, verbose_name="Correo cliente", default=None)
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    clie_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    def __str__(self):
        return "%s %s" %(self.clie_nombre, self.clie_apellido)
    
class Venta(models.Model):
    vent_id = models.AutoField(primary_key=True, default=None)
    vent_fecha = models.DateField(verbose_name="Fecha venta")
    vent_cliente = models.CharField(max_length=45, verbose_name="Cliente", default=None)
    vent_precio_subtotal = models.IntegerField(verbose_name="SubTotal venta", default=None)
    vent_iva = models.IntegerField(verbose_name="Iva de la venta", default=None)
    vent_precio_total = models.IntegerField(verbose_name="Precio total de la venta", default=None)
    class Estado(models.TextChoices):
        ACTIVO ='1', _('Activo')
        INACTIVO ='0', _('Inactivo')
    vent_estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    Cliente_clie_id = models.ForeignKey(Cliente, verbose_name="Id cliente", on_delete=models.CASCADE, default=None)
    Usuario_usu_id = models.ForeignKey(Usuario, verbose_name="Id Usuario", on_delete=models.CASCADE, default=None)
    
    
class Detalle_Venta(models.Model): #Falta venta_has_clientecol y venta_vent_id "autoincrementable"
    det_vent_id = models.AutoField(primary_key=True, default=None)
    det_vent_precio_unitario = models.IntegerField(verbose_name="Precio unitario del producto", default=None)
    det_vent_cantidad = models.IntegerField(verbose_name="Cantidad vendida", default=None)
    det_vent_precio_total = models.IntegerField(verbose_name="Precio total del producto", default=None)
    Servicios_serv_id = models.ForeignKey(Servicio, null=True, verbose_name="Id Servicio", on_delete=models.CASCADE, default=None)
    Producto_producto_id = models.ForeignKey(Producto, null=True, verbose_name="Id Producto", on_delete=models.CASCADE, default=None)
    Venta_vent_id = models.ForeignKey(Venta,  verbose_name="Id Venta", on_delete=models.CASCADE, default=None)