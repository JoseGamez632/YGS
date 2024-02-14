# Generated by Django 4.2.3 on 2024-02-14 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_remove_insumo_stock_remove_insumo_stock_min_and_more'),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='clie_direccion',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='id',
        ),
        migrations.RemoveField(
            model_name='detalle_venta',
            name='cliente_clie_id',
        ),
        migrations.RemoveField(
            model_name='detalle_venta',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='detalle_venta',
            name='id',
        ),
        migrations.RemoveField(
            model_name='detalle_venta',
            name='vent_id',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='id',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='usu_id',
        ),
        migrations.AddField(
            model_name='cliente',
            name='clie_estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='clie_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='Producto_producto_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.producto', verbose_name='Id Producto'),
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='Servicios_serv_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.servicio', verbose_name='Id Servicio'),
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='Venta_vent_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ventas.venta', verbose_name='Id Venta'),
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='det_vent_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='det_vent_precio_total',
            field=models.IntegerField(default=None, verbose_name='Precio total del producto'),
        ),
        migrations.AddField(
            model_name='venta',
            name='Cliente_clie_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ventas.cliente', verbose_name='Id cliente'),
        ),
        migrations.AddField(
            model_name='venta',
            name='Usuario_usu_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name='Id Usuario'),
        ),
        migrations.AddField(
            model_name='venta',
            name='vent_cliente',
            field=models.CharField(default=None, max_length=45, verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='venta',
            name='vent_estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='venta',
            name='vent_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='clie_apellido',
            field=models.CharField(default=None, max_length=45, verbose_name='Apellido proveedor'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='clie_correo_electronico',
            field=models.CharField(default=None, max_length=45, verbose_name='Correo cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='clie_nombre',
            field=models.CharField(default=None, max_length=45, verbose_name='Nombre cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='clie_num_documento',
            field=models.CharField(default=None, max_length=16, verbose_name='Numero documento cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='clie_telefono',
            field=models.CharField(default=None, max_length=45, verbose_name='Telefono Cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='clie_tipo_documento',
            field=models.CharField(choices=[(0, 'Cedula de Ciudadania'), (1, 'Cedula de Extranjeria'), (2, 'Permiso de permanencia'), (3, 'Pasaporte'), (4, 'Numero Identificacion Tributaria'), (5, 'Otro')], default=0, max_length=1, verbose_name='Tipo de documento del cliente'),
        ),
        migrations.AlterField(
            model_name='detalle_venta',
            name='det_vent_cantidad',
            field=models.IntegerField(default=None, verbose_name='Cantidad vendida'),
        ),
        migrations.AlterField(
            model_name='detalle_venta',
            name='det_vent_precio_unitario',
            field=models.IntegerField(default=None, verbose_name='Precio unitario del producto'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='vent_fecha',
            field=models.DateField(verbose_name='Fecha venta'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='vent_iva',
            field=models.IntegerField(default=None, verbose_name='Iva de la venta'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='vent_precio_subtotal',
            field=models.IntegerField(default=None, verbose_name='SubTotal venta'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='vent_precio_total',
            field=models.IntegerField(default=None, verbose_name='Precio total de la venta'),
        ),
    ]