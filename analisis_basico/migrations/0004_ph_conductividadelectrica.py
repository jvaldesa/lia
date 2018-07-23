# Generated by Django 2.0.5 on 2018-06-22 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recepcion', '0002_auto_20180604_1524'),
        ('analisis_basico', '0003_folios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ph_ConductividadElectrica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph', models.DecimalField(decimal_places=2, max_digits=4)),
                ('clasificacion_ph', models.CharField(blank=True, max_length=100, null=True)),
                ('ce', models.DecimalField(decimal_places=2, max_digits=7)),
                ('unidad', models.CharField(max_length=50)),
                ('clasificacion_ce', models.CharField(blank=True, max_length=100, null=True)),
                ('folio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recepcion.Recepcion')),
            ],
        ),
    ]
