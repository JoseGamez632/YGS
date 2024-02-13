from django.db import models
from django.utils.translation import gettext_lazy as _
from usuarios.models import Usuario, Insumo

# Proveedor terminado
class Proveedor(models.Model): 
    prov_id = models.AutoField(primary_key=True)
    prov_nombre = models.CharField(max_length=45, verbose_name="Nombre del proveedor")
    prov_nit = models.CharField(max_length=16, verbose_name="NIT del proveedor")
    prov_telefono = models.CharField(max_length=45, verbose_name="Telefono de proveedor")
    prov_encargado = models.CharField(max_length=45, verbose_name="Encargado  del proveedor")
    prov_tipo_documento = models.CharField(max_length=15, verbose_name="Tipo de identificación del proveedor")
    prov_num_documento = models.CharField(max_length=16, verbose_name="Numero de odentificación")
    class estProveedor(models.IntegerChoices):
        ACTIVO = 1, _("Activo")
        INACTIVO = 0, _("Inactivo")
    prov_estado = models.CharField(max_length=1, choices=estProveedor.choices, default=estProveedor.ACTIVO, verbose_name="Estado del proveedor")
    
    def __str__(self):
        return "%s %s" %(self.prov_nombre)
    

class Compra(models.Model):
    comp_id = models.AutoField(primary_key=True)
    comp_fecha = models.DateField(verbose_name="Fecha de compra")
    comp_nombre_proveedor = models.CharField(max_length=45, verbose_name="Nombre  del Proveedor")
    comp_precio_total = models.IntegerField(verbose_name="Precio total de la compra")
    class medPagoComp (models.IntegerChoices):
        EFECTIVO = 0, _("Efectivo")
        TRANSFERENCIA = 1, _("Transferencia")
        TARJETA = 2, _("Tarjetas Debito o Credito")
        TRANSFERENCIABANCARIA =  3, _("Transferencia Bancaria")
        CHEQUE = 4, _("Cheque")
    comp_medio_pago = models.CharField(max_length=1, choices=medPagoComp.choices, default=medPagoComp.EFECTIVO, verbose_name="Medio de pago de compra")
    class estCompra (models.IntegerChoices):
        ACTIVO = 1, _("Activo")
        INACTIVO = 0, _("Inactivo")
    comp_estado = models.CharField(max_length=1, choices=estCompra.choices, default=estCompra.ACTIVO, verbose_name="Estado de la compra")
    Usuario_usu_id = models.ForeignKey(Usuario, verbose_name="UsuarioCompID", on_delete=models.PROTECT, related_name='UsuarioComID')
    Proveedor_prov_id = models.ForeignKey(Proveedor, verbose_name="proveedor", on_delete=models.PROTECT, related_name='proveedor')
    
    
class Detalle_compra(models.Model): 
    det_comp_id = models.AutoField(primary_key=True)
    det_comp_precio_unitario = models.IntegerField(verbose_name="Precio unitario")
    det_comp_cantidad = models.IntegerField(verbose_name="Cantidad")
    det_comp_precio_total = models.IntegerField(verbose_name="Procio total")
    Insumos_insumos_id = models.ForeignKey(Insumo, verbose_name="id insumo")
    Compra_comp_id = models.ForeignKey(Compra, verbose_name="Id Compra")