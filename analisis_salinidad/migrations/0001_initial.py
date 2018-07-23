# Generated by Django 2.0.5 on 2018-07-06 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('generales', '0008_auto_20180622_1254'),
        ('recepcion', '0002_auto_20180604_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aniones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulacionCar', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Titulación Carbonatos')),
                ('titulacionBlancoCar', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Titulación Blanco')),
                ('normalidadH2SO4', models.DecimalField(decimal_places=3, max_digits=7, verbose_name='Normalidad H2SO4')),
                ('alicuotaCar', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Alicuota')),
                ('titulacionBic', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Titulación Bicarbonatos')),
                ('titulacionBlancoBic', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Titulación Blanco')),
                ('alicuotaBic', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Alicuota')),
                ('titulacionClo', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Titulación Cloruros')),
                ('titulacionBlancoClo', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Titulación Blanco')),
                ('normalidadAgNO3', models.DecimalField(decimal_places=3, max_digits=7, verbose_name='Normalidad AgNO3')),
                ('alicuotaClo', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Alicuota')),
                ('conductividadEl', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Coductividad Eléctrica')),
                ('unidad', models.CharField(max_length=50, verbose_name='Unidad')),
                ('carbonatos', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Carbonatos (meq/L)')),
                ('bicarbonatos', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Bicarbonatos (meq/L)')),
                ('cloruros', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Cloruros (meq/L)')),
                ('sulfatos', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Sulfatos (meq/L)')),
                ('fecha_analisis', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
                ('analista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='generales.Analista')),
                ('folio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recepcion.Recepcion')),
            ],
        ),
        migrations.CreateModel(
            name='Cationes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulacionCaMg', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Titulación Ca+Mg (ml)')),
                ('normalidadEDTA', models.DecimalField(decimal_places=2, default=0.01, max_digits=7, verbose_name='Normalidad EDTA')),
                ('titulacionCa', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Titulación Ca (ml)')),
                ('alicuota', models.DecimalField(decimal_places=2, default=5, max_digits=7, verbose_name='Alicuota')),
                ('Na', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Na (ppm)')),
                ('K', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='K (ppm)')),
                ('CaCation', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Ca++ (meq/L)')),
                ('MgCation', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Mg++ (meq/L)')),
                ('NaCation', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Na+ (meq/L)')),
                ('KCation', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='K+ (meq/L)')),
                ('fecha_analisis', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
                ('analista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='generales.Analista')),
                ('folio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recepcion.Recepcion')),
            ],
        ),
        migrations.CreateModel(
            name='PhCePasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph', models.DecimalField(decimal_places=2, max_digits=4)),
                ('ce', models.DecimalField(decimal_places=2, max_digits=7)),
                ('unidad', models.CharField(max_length=50)),
                ('fecha_analisis', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
                ('analista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='generales.Analista')),
                ('folio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recepcion.Recepcion')),
            ],
        ),
    ]
