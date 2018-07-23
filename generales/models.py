
from django.db import models

# Create your models here.


class Analista(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Cultivo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ['nombre']

class Estado(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=200)


    def __str__(self):
        return self.nombre


class Organizacion(models.Model):
    nombre = models.CharField(max_length=200)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True)
    localidad = models.CharField(max_length=200, blank=True, null=True)
    calle = models.CharField(max_length=200, blank=True, null=True)
    numero_exterior = models.CharField(max_length=20, blank=True, null=True)
    numero_interior = models.CharField(max_length=20, blank=True, null=True)
    colonia = models.CharField(max_length=200, blank=True, null=True)
    codigo_postal = models.PositiveIntegerField(blank=True, null=True)
    rfc = models.CharField(max_length=20, blank=True, null=True)
    telefono_1  = models.CharField(max_length=20, blank=True, null=True)
    telefono_2 = models.CharField(max_length=20, blank=True, null=True)
    telefono_3 = models.CharField(max_length=20, blank=True, null=True)
    correo_electronico_1 = models.EmailField(blank=True, null=True)
    correo_electronico_2 = models.EmailField(blank=True, null=True)
    contacto_1 = models.CharField(max_length=100, blank=True, null=True)
    puesto_contacto_1 = models.CharField(max_length=100, blank=True, null=True)
    telefono_contacto1 = models.CharField(max_length=20, blank=True, null=True)
    correo_electronico_contacto_1 = models.EmailField(blank=True, null=True)
    contacto_2 = models.CharField(max_length=100, blank=True, null=True)
    puesto_contacto_2 = models.CharField(max_length=100, blank=True, null=True)
    telefono_contacto_2 = models.CharField(max_length=20, blank=True, null=True)
    correo_electronico_contacto_2 = models.EmailField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name_plural = 'Organizaciones'

    def __str__(self):
        return self.nombre


class RegimenHidrico(models.Model):
    nombre = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    def __str__(self):
        return self.nombre


class TipoAnalisis(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    def __str__(self):
        return self.nombre
