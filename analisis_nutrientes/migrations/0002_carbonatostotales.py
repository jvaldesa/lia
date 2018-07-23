# Generated by Django 2.0.5 on 2018-07-02 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0002_auto_20180604_1524'),
        ('generales', '0008_auto_20180622_1254'),
        ('analisis_nutrientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarbonatosTotales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m', models.DecimalField(decimal_places=2, default=0.1, max_digits=5, verbose_name='Molaridad de la solución')),
                ('a', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='ml Titulación Blanco')),
                ('b', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='ml Titulación Muestra')),
                ('s', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Peso de la Muestra')),
                ('CaCo3', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('fecha_analisis', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
                ('analista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='generales.Analista')),
                ('folio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recepcion.Recepcion')),
            ],
        ),
    ]
