# Generated by Django 2.0.5 on 2018-06-01 16:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0002_auto_20180531_1930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizacion',
            options={'verbose_name_plural': 'Organizaciones'},
        ),
        migrations.AddField(
            model_name='organizacion',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de Creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organizacion',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición'),
        ),
        migrations.AlterField(
            model_name='organizacion',
            name='codigo_postal',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]