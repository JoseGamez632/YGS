from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import Usuario

# Create your models here.
class proveedor(models.Model): #Falta proveedor_id autoinclementable
    prov_nombre = models.CharField(max_length=45, verbose_name="Nombre proveedor")
    prov_apellido = models.CharField(max_length=45, verbose_name="Apellido proveedor")
    prov_nit = models.CharField(max_length=45, verbose_name="nit proveedor")
    prov_telefono = models.CharField(max_length=15, verbose_name="Teléfono proveedor")
    prov_direccion = models.CharField(max_length=45, verbose_name="Dirección proveedor")
    class metPago(models.IntegerChoices):
        EF = 0, _('Efectivo')
        TC = 1, _('Tarjeta de crédito')
        CH = 2, _('Cheque')
        TB = 3, _('Transferencia bancaria')
    prov_metodo_pago = models.IntegerField(default=metPago.EF, choices=metPago.choices, verbose_name="Metodo de pago")
    class TipoDoc(models.IntegerChoices):
        CC = 0, _('CC')
        CE = 1, _('CE')
        PEP = 2, _('PEP')
        PA = 3, _('PA')
        NIT = 4, _('NIT')
        OT = 5, _('OTRO')
    prov_tipo_documento = models.IntegerField(default=TipoDoc.CC, choices=TipoDoc.choices, verbose_name="Tipo documento")
    prov_num_documento = models.CharField(max_length=25, verbose_name="Número de documento")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    def __str__(self):
        return "%s %s" %(self.prov_nombre, self.prov_apellido)
    
class compra(models.Model):
    usu_id = models.ForeignKey(Usuario, verbose_name="UsuarioComID", on_delete=models.PROTECT, related_name='UsuarioComID')
    prov_id = models.ForeignKey(proveedor, verbose_name="proveedor", on_delete=models.PROTECT, related_name='proveedor')
    comp_fecha = models.DateField(verbose_name="Fecha de compra")
    # comp_precio_subtotal = models.IntegerField(verbose_name="Precio subtotal")
    # comp_iva = models.IntegerField(verbose_name="IVA")
    comp_precio_total = models.IntegerField(verbose_name="Compra, costo total")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    
class Detalle_compra(models.Model): 
    comp_id = models.ForeignKey(compra, on_delete=models.PROTECT, verbose_name="Número de compra", related_name="Numcompra")
    usu_id = models.ForeignKey(Usuario, on_delete=models.PROTECT, verbose_name="ID_usuario", related_name="ID_usuario")
    det_comp_precio_unitario = models.IntegerField(verbose_name="Precio unitario del insumo")
    det_comp_cantidad = models.IntegerField(verbose_name="Cantidad producto")
    det_comp_precio_total = models.IntegerField(verbose_name="Compra, costo total")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
