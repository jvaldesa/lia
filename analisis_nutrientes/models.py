from django.db import models
from recepcion.models import Recepcion
from generales.models import Analista




# Create your models here.
class Nitrogeno(models.Model):
    folio = models.OneToOneField(Recepcion, on_delete=models.CASCADE)
    M = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='ml de Titulación')
    B = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='ml de Blanco')
    N = models.DecimalField(max_digits=5, decimal_places=3, verbose_name='Normalidad del acido', default=0.005)
    Vi = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Volumen Extractante', default=50)
    a = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Alicuota Destilada', default=10)
    p = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Peso de Muestra', default=5)
    nitrogeno = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    analista = models.ForeignKey(Analista, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_analisis = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    def __str__(self):
        return str(self.folio)



class CarbonatosTotales(models.Model):
    folio = models.OneToOneField(Recepcion, on_delete=models.CASCADE)
    m = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Molaridad de la solución', default=0.1)
    a = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='ml Titulación Blanco')
    b = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='ml Titulación Muestra')
    s = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Peso de la Muestra')
    CaCo3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    analista = models.ForeignKey(Analista, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_analisis = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    def __str__(self):
        return str(self.folio)



class Micronutrientes(models.Model):
    folio = models.OneToOneField(Recepcion, on_delete=models.CASCADE)
    Fe = models.DecimalField(max_digits=7, decimal_places=2)
    Cu = models.DecimalField(max_digits=7, decimal_places=2)
    Mn = models.DecimalField(max_digits=7, decimal_places=2)
    Zn = models.DecimalField(max_digits=7, decimal_places=2)
    analista = models.ForeignKey(Analista, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_analisis = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    def __str__(self):
        return str(self.folio)



class BasesIntercambiables(models.Model):
    folio = models.OneToOneField(Recepcion, on_delete=models.CASCADE)
    Ca = models.DecimalField(max_digits=7, decimal_places=2)
    Mg = models.DecimalField(max_digits=7, decimal_places=2)
    Na = models.DecimalField(max_digits=7, decimal_places=2)
    K = models.DecimalField(max_digits=7, decimal_places=2)
    analista = models.ForeignKey(Analista, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_analisis = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    def __str__(self):
        return str(self.folio)



class Fosforo(models.Model):
    folio = models.OneToOneField(Recepcion, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    fosforo = models.DecimalField(max_digits=7, decimal_places=2)
    analista = models.ForeignKey(Analista, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_analisis = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    def __str__(self):
        return str(self.folio)


