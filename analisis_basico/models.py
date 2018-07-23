from django.db import models
from generales.models import Analista
from recepcion.models import Recepcion

# Create your models here.


# ----TEXTURA
class Textura(models.Model):
    folio = models.OneToOneField(Recepcion, on_delete=models.CASCADE)
    lectura_1 = models.DecimalField(max_digits=5, decimal_places=2)
    lectura_2 = models.DecimalField(max_digits=5, decimal_places=2)
    lectura_3 = models.DecimalField(max_digits=5, decimal_places=2)
    lectura_4 = models.DecimalField(max_digits=5, decimal_places=2)
    temperatura_1 = models.DecimalField(max_digits=5, decimal_places=2)
    temperatura_2 = models.DecimalField(max_digits=5, decimal_places=2)
    temperatura_3 = models.DecimalField(max_digits=5, decimal_places=2)
    temperatura_4 = models.DecimalField(max_digits=5, decimal_places=2)
    arenas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    arcillas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    limos = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    textura = models.CharField(max_length=100, blank=True, null=True)
    analista = models.ForeignKey(Analista, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_analisis = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    def __str__(self):
        return str(self.folio)
    

#---- PH Y CONDUCTIVIDAD ELECTRICA
class Ph_ConductividadElectrica(models.Model):
    folio = models.OneToOneField(Recepcion, on_delete=models.CASCADE)
    ph = models.DecimalField(max_digits=4, decimal_places=2)
    clasificacion_ph = models.CharField(max_length=100, blank=True, null=True)
    ce = models.DecimalField(max_digits=7, decimal_places=2)
    unidad = models.CharField(max_length=50)
    clasificacion_ce = models.CharField(max_length=100, blank=True, null=True)
    analista = models.ForeignKey(Analista, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_analisis = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    def __str__(self):
        return str(self.folio)


#---- MATERIA ORGANICA
class MateriaOrganica(models.Model):
    folio = models.OneToOneField(Recepcion, on_delete=models.CASCADE)
    clase_suelo = models.CharField(max_length=100)
    b1 = models.DecimalField(max_digits=5, decimal_places=2)
    b2 = models.DecimalField(max_digits=5, decimal_places=2)
    b3 = models.DecimalField(max_digits=5, decimal_places=2)
    t = models.DecimalField(max_digits=5, decimal_places=2)
    g = models.DecimalField(max_digits=5, decimal_places=2)
    N = models.DecimalField(max_digits=5, decimal_places=2)
    materia_organica = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    interpretacion =  models.CharField(max_length=100, blank=True, null=True)
    analista = models.ForeignKey(Analista, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_analisis = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    def __str__(self):
        return str(self.folio)


#---- COLOR Y DENSIDAD APARENTE
class ColorDensidadAparente(models.Model):
    folio = models.OneToOneField(Recepcion, on_delete=models.CASCADE)
    clave = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    peso =  models.DecimalField(max_digits=5, decimal_places=2)
    volumen =  models.DecimalField(max_digits=5, decimal_places=2)
    densidad_aparente =  models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    analista = models.ForeignKey(Analista, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_analisis = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    def __str__(self):
        return str(self.folio)


#---- PUNTO DE SATURACION
class PuntoSaturacion(models.Model):
    folio = models.OneToOneField(Recepcion, on_delete=models.CASCADE)
    peso_inicial_estufa =  models.DecimalField(max_digits=5, decimal_places=2, default=50)
    peso_final_estufa =  models.DecimalField(max_digits=5, decimal_places=2)
    agua_gastada_estufa =  models.DecimalField(max_digits=5, decimal_places=2)
    peso_inicial_aire =  models.DecimalField(max_digits=5, decimal_places=2, default=50)
    peso_final_aire =  models.DecimalField(max_digits=5, decimal_places=2)
    agua_gastada_aire =  models.DecimalField(max_digits=5, decimal_places=2)
    punto_saturacion =  models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    capacidad_campo =  models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    punto_marchitez =  models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    analista = models.ForeignKey(Analista, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_analisis = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    def __str__(self):
        return str(self.folio)












# EJERCICIO DE CONSULTA DE RESULTADOS   
class Folios(models.Model):
    folio = models.ForeignKey(Recepcion, on_delete=models.CASCADE)