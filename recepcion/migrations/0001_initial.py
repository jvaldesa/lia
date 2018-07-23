# Generated by Django 2.0.5 on 2018-06-01 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('generales', '0004_auto_20180601_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recepcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.CharField(max_length=50, unique=True)),
                ('productor', models.CharField(max_length=200)),
                ('fecha_recepcion', models.DateField(blank=True, null=True)),
                ('fecha_muestreo', models.DateField(blank=True, null=True)),
                ('profundida_cm', models.PositiveIntegerField(blank=True, null=True)),
                ('numero_hectareas', models.DecimalField(blank=True, decimal_places=4, max_digits=8, null=True)),
                ('cultivo_anterior', models.CharField(blank=True, max_length=100, null=True)),
                ('cultivo_a_establecer', models.CharField(blank=True, max_length=100, null=True)),
                ('rendimiento_esperado', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('localidad_ejido', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='generales.Estado')),
                ('municipio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='generales.Municipio')),
                ('organizacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='generales.Organizacion')),
                ('regimen_hidrico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='generales.RegimenHidrico')),
                ('tipo_analisis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='generales.TipoAnalisis')),
            ],
            options={
                'verbose_name_plural': 'Recepciones',
            },
        ),
    ]