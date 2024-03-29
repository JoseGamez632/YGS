# Generated by Django 4.2.3 on 2024-02-14 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insumo',
            name='Stock',
        ),
        migrations.RemoveField(
            model_name='insumo',
            name='Stock_min',
        ),
        migrations.RemoveField(
            model_name='insumo',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='insumo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='insumo',
            name='insum_cantidad',
        ),
        migrations.RemoveField(
            model_name='insumo',
            name='insum_categoria',
        ),
        migrations.RemoveField(
            model_name='insumo',
            name='insum_codigo',
        ),
        migrations.RemoveField(
            model_name='insumo',
            name='insum_pre_compra',
        ),
        migrations.RemoveField(
            model_name='insumo',
            name='insum_total',
        ),
        migrations.RemoveField(
            model_name='insumo',
            name='usu_id',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='Stock',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='Stock_min',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='id',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='prod_codigo',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='prod_descripcion',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='prod_pre_compra',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='prod_pre_venta',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='usu_id',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='id',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='serv_categoria',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='serv_codigo',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='serv_pago_total',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='usu_id',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='usu_apellido',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='usu_email',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='usu_nombre',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='usu_num_doc',
        ),
        migrations.AddField(
            model_name='insumo',
            name='Usuario_usu_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name='ID Usuario'),
        ),
        migrations.AddField(
            model_name='insumo',
            name='insum_estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='insumo',
            name='insum_precio',
            field=models.IntegerField(default=None, verbose_name='Precio del insumo'),
        ),
        migrations.AddField(
            model_name='insumo',
            name='insumos_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='producto',
            name='Usuario_usu_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name='Id Usuario'),
        ),
        migrations.AddField(
            model_name='producto',
            name='prod_costo_prod',
            field=models.IntegerField(default=None, verbose_name='Costo del producto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='prod_estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='producto',
            name='prod_precio_venta',
            field=models.IntegerField(default=None, verbose_name='Precio de venta'),
        ),
        migrations.AddField(
            model_name='producto',
            name='producto_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='servicio',
            name='Usuario_usu_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name='Id Usuario'),
        ),
        migrations.AddField(
            model_name='servicio',
            name='serv_estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='servicio',
            name='serv_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='servicio',
            name='serv_precio',
            field=models.IntegerField(default=None, verbose_name='Precio del servicio'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='usu_correo_electronico',
            field=models.CharField(default=None, max_length=45, verbose_name='Correo electronico de usuario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='usu_estado',
            field=models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='usu_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='usu_nombre_apellido',
            field=models.CharField(default=None, max_length=45, verbose_name='Nombre y apellido'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='usu_nombre_usuario',
            field=models.CharField(default=None, max_length=45, verbose_name='Nombre de Usuario'),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='insum_nombre',
            field=models.CharField(default=None, max_length=45, verbose_name='Nombre del insumo'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='prod_nombre',
            field=models.CharField(default=None, max_length=45, verbose_name='Nombre del producto'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='serv_descripcion',
            field=models.CharField(default=None, max_length=260, verbose_name='Descripción del servicio'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='serv_nombre',
            field=models.CharField(default=None, max_length=45, verbose_name='Nombre de servicio'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usu_clave',
            field=models.CharField(default=None, max_length=30, verbose_name='Contrasenia de acceso'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usu_direccion',
            field=models.CharField(default=None, max_length=45, verbose_name='Dirección de usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usu_num_documento',
            field=models.IntegerField(default=None, verbose_name='Numero de documento'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usu_telefono',
            field=models.CharField(default=None, max_length=45, verbose_name='Telefono de usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usu_tipo_documento',
            field=models.CharField(choices=[(0, 'CC'), (1, 'CE'), (2, 'PP')], default=0, max_length=1, verbose_name='Tipo documento'),
        ),
        migrations.AddField(
            model_name='insumo',
            name='stock',
            field=models.IntegerField(default=None, verbose_name='Stock de insumos'),
        ),
        migrations.AddField(
            model_name='insumo',
            name='stock_min',
            field=models.IntegerField(default=None, verbose_name='Stock minimo de insumos'),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=None, verbose_name='Stock'),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock_min',
            field=models.IntegerField(default=None, verbose_name='Stock minimo'),
        ),
    ]
