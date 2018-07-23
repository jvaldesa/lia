# Generated by Django 2.0.5 on 2018-06-26 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0008_auto_20180622_1254'),
        ('recepcion', '0002_auto_20180604_1524'),
        ('analisis_basico', '0007_colordensidadaparente'),
    ]

    operations = [
        migrations.CreateModel(
            name='PuntoSaturacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso_inicial_estufa', models.DecimalField(decimal_places=2, max_digits=5)),
                ('peso_final_estufa', models.DecimalField(decimal_places=2, max_digits=5)),
                ('agua_gastada_estufa', models.DecimalField(decimal_places=2, max_digits=5)),
                ('peso_inicial_aire', models.DecimalField(decimal_places=2, max_digits=5)),
                ('peso_final_aire', models.DecimalField(decimal_places=2, max_digits=5)),
                ('agua_gastada_aire', models.DecimalField(decimal_places=2, max_digits=5)),
                ('punto_saturacion', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('capacidad_campo', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('punto_marchitez', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('fecha_analisis', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
                ('analista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='generales.Analista')),
                ('folio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recepcion.Recepcion')),
            ],
        ),
    ]
