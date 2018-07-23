from django.db import models
from generales.models import Estado, Municipio, TipoAnalisis, Organizacion, RegimenHidrico, Cultivo
# Create your models here.


class Recepcion(models.Model):
    folio = models.CharField(max_length=50, unique=True)
    productor = models.CharField(max_length=200)
    organizacion = models.ForeignKey(Organizacion, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_recepcion = models.DateField(blank=True, null=True)
    fecha_muestreo = models.DateField(blank=True, null=True)
    tipo_analisis = models.ForeignKey(TipoAnalisis, on_delete=models.SET_NULL, blank=True, null=True)
    regimen_hidrico = models.ForeignKey(RegimenHidrico, on_delete=models.SET_NULL, blank=True, null=True)
    profundida_cm = models.PositiveIntegerField(blank=True, null=True)
    numero_hectareas = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    cultivo_anterior = models.ForeignKey(Cultivo, on_delete=models.CASCADE,related_name='cultivo_anterior', blank=True, null=True)
    cultivo_a_establecer =  models.ForeignKey(Cultivo, on_delete=models.CASCADE, related_name='cultivo_nuevo', blank=True, null=True)
    rendimiento_esperado = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, blank=True, null=True)
    municipio =  models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True)
    localidad_ejido = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')
    
    class Meta:
        verbose_name_plural = 'Recepciones'

    def __str__(self):
        return 'Folio: {}'.format(self.folio)