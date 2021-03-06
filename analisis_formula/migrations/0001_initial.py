# Generated by Django 2.0.5 on 2018-07-10 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recepcion', '0002_auto_20180604_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasesCambio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CaMeq', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Ca+ (meq/100g)')),
                ('MgMeq', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Mg++ (meq/100g)')),
                ('NaMeq', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Na+ (meq/100g)')),
                ('KMeq', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='K+ (meq/100g)')),
                ('Cic', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Capacidad de Intercambio Cationico (CIC')),
                ('CaPorcentaje', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Ca+ (%)')),
                ('MgPorcentaje', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Mg+ (%)')),
                ('NaPorcentaje', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Na+ (%)')),
                ('KPorcentaje', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='K+ (%)')),
                ('Ca_Mg', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Ca/Mg')),
                ('Mg_K', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Mg/K')),
                ('CaMg_K', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='(Ca+Mg)/K')),
                ('Ca_K', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Ca/K')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
                ('folio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recepcion.Recepcion')),
            ],
        ),
        migrations.CreateModel(
            name='RasPsi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ras', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='RAS')),
                ('Psi', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='PSI')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
                ('folio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recepcion.Recepcion')),
            ],
        ),
    ]
