from django.db import models
from recepcion.models import Recepcion
from generales.models import Analista
# Create your models here.


#---- PH Y CONDUCTIVIDAD ELECTRICA PASTA DE SATURACION
class PhCePasta(models.Model):
    folio = models.OneToOneField(Recepcion, on_delete=models.CASCADE)
    ph = models.DecimalField(max_digits=4, decimal_places=2)
    ce = models.DecimalField(max_digits=7, decimal_places=2)
    unidad = models.CharField(max_length=50)
    analista = models.ForeignKey(Analista, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_analisis = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    def __str__(self):
        return str(self.folio)



#---- CATIONES
class Cationes(models.Model):
    folio = models.OneToOneField(Recepcion, on_delete=models.CASCADE)
    titulacionCaMg = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Titulación Ca+Mg (ml)')
    normalidadEDTA = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Normalidad EDTA', default=0.01)
    titulacionCa = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Titulación Ca (ml)')
    alicuota = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Alicuota', default=5)
    Na = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Na (ppm)')
    K = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='K (ppm)')
    CaCation = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Ca++ (meq/L)', blank=True, null=True)
    MgCation = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Mg++ (meq/L)', blank=True, null=True)
    NaCation = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Na+ (meq/L)', blank=True, null=True)
    KCation = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='K+ (meq/L)', blank=True, null=True)
    analista = models.ForeignKey(Analista, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_analisis = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    def __str__(self):
        return str(self.folio)


#---- ANIONES
class Aniones(models.Model):
    folio = models.OneToOneField(Recepcion, on_delete=models.CASCADE)
    titulacionCar = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Titulación Carbonatos')
    titulacionBlancoCar = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Titulación Blanco')
    normalidadH2SO4 = models.DecimalField(max_digits=7, decimal_places=3, verbose_name='Normalidad H2SO4')
    alicuotaCar = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Alicuota')
    titulacionBic = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Titulación Bicarbonatos')
    titulacionBlancoBic = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Titulación Blanco')
    alicuotaBic = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Alicuota')
    titulacionClo = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Titulación Cloruros')
    titulacionBlancoClo = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Titulación Blanco')
    normalidadAgNO3 = models.DecimalField(max_digits=7, decimal_places=3, verbose_name='Normalidad AgNO3')
    alicuotaClo = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Alicuota')
    conductividadEl = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Coductividad Eléctrica')
    unidad = models.CharField(max_length=50, verbose_name='Unidad')
    carbonatos = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Carbonatos (meq/L)', blank=True, null=True)
    bicarbonatos = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Bicarbonatos (meq/L)', blank=True, null=True)
    cloruros = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Cloruros (meq/L)', blank=True, null=True)
    sulfatos = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Sulfatos (meq/L)', blank=True, null=True)
    analista = models.ForeignKey(Analista, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_analisis = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')


    def __str__(self):
        return str(self.folio)
