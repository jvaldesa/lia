# Generated by Django 2.0.5 on 2018-08-09 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultadostotal',
            name='ph',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]