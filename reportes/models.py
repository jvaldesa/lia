from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from recepcion.models import Recepcion
from analisis_basico.models import Textura,Ph_ConductividadElectrica, MateriaOrganica, ColorDensidadAparente, PuntoSaturacion
from analisis_nutrientes.models import Nitrogeno, CarbonatosTotales, Micronutrientes, BasesIntercambiables, Fosforo
from analisis_salinidad.models import PhCePasta, Cationes, Aniones
from analisis_formula.models import BasesCambio, RasPsi
from calculos.reportes import generadorCadenaConsulta, extraccionValor as ex
from generales.models import Organizacion, Cultivo, Estado, Municipio, RegimenHidrico, TipoAnalisis


# Create your models here.
class ResultadosTotal(models.Model):
    slug = models.SlugField(max_length=10, unique=True, blank=True, null=True)
    folio = models.OneToOneField(Recepcion, on_delete=models.CASCADE)
    folio_str = models.CharField(max_length=50, blank=True, null=True)
    productor = models.CharField(max_length=200, blank=True, null=True)
    organizacion = models.CharField(max_length=200, blank=True, null=True)
    fecha_recepcion = models.DateField(blank=True, null=True)
    fecha_muestreo = models.DateField(blank=True, null=True)
    tipo_analisis =  models.CharField(max_length=100, blank=True, null=True)
    regimen_hidrico =  models.CharField(max_length=100, blank=True, null=True)
    profundida_cm = models.PositiveIntegerField(blank=True, null=True)
    numero_hectareas = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    cultivo_anterior =  models.CharField(max_length=100, blank=True, null=True)
    cultivo_a_establecer =   models.CharField(max_length=100, blank=True, null=True)
    rendimiento_esperado = models.DecimalField(max_digits=9, decimal_places=4, blank=True, null=True)
    estado =  models.CharField(max_length=200, blank=True, null=True)
    municipio = models.CharField(max_length=200, blank=True, null=True)
    localidad_ejido = models.CharField(max_length=200, blank=True, null=True)
    nombre_predio = models.CharField(max_length=200, blank=True, null=True)
    textura_arenas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    textura_arcillas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    textura_limos = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    textura_textura = models.CharField(max_length=100, blank=True, null=True)
    ph = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    clasificacion_ph = models.CharField(max_length=100, blank=True, null=True)
    ce = models.DecimalField(max_digits=7, decimal_places=2,blank=True, null=True)
    unidad = models.CharField(max_length=50, blank=True, null=True)
    clasificacion_ce = models.CharField(max_length=100, blank=True, null=True)
    materia_organica = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    interpretacionMO =  models.CharField(max_length=100, blank=True, null=True)
    clave_color = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    densidad_aparente =  models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    punto_saturacion =  models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    capacidad_campo =  models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    punto_marchitez =  models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nitrogeno = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    CaCo3 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Carbonatos Totales')
    Fe = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    Cu = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    Mn = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    Zn = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    Ca = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    Mg = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    Na = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    K = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    tipo_fosforo = models.CharField(max_length=100, blank=True, null=True)
    fosforo = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    ph_pasta = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ce_pasta = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    unidad_cePasta = models.CharField(max_length=50, blank=True, null=True)
    CaCation = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Ca++ (meq/L)', blank=True, null=True)
    MgCation = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Mg++ (meq/L)', blank=True, null=True)
    NaCation = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Na+ (meq/L)', blank=True, null=True)
    KCation = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='K+ (meq/L)', blank=True, null=True)
    carbonatos = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Carbonatos (meq/L)', blank=True, null=True)
    bicarbonatos = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Bicarbonatos (meq/L)', blank=True, null=True)
    cloruros = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Cloruros (meq/L)', blank=True, null=True)
    sulfatos = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Sulfatos (meq/L)', blank=True, null=True)
    CaMeq = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Ca+ (meq/100g)', blank=True, null=True)
    MgMeq = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Mg++ (meq/100g)', blank=True, null=True)
    NaMeq = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Na+ (meq/100g)', blank=True, null=True)
    KMeq = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='K+ (meq/100g)', blank=True, null=True)
    Cic = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Capacidad de Intercambio Cationico (CIC)', blank=True, null=True)
    CaPorcentaje = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Ca+ (%)', blank=True, null=True)
    MgPorcentaje = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Mg+ (%)', blank=True, null=True)
    NaPorcentaje = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Na+ (%)', blank=True, null=True)
    KPorcentaje = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='K+ (%)', blank=True, null=True)
    Ca_Mg = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Ca/Mg', blank=True, null=True)
    Mg_K = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Mg/K', blank=True, null=True)
    CaMg_K = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='(Ca+Mg)/K', blank=True, null=True)
    Ca_K = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Ca/K', blank=True, null=True)
    Ras = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='RAS', blank=True, null=True)
    Psi = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='PSI', blank=True, null=True)

    def __str__(self):
        return str(self.folio)



 # --- RECEPCION   

@receiver(post_save, sender=Recepcion)
def folio(sender, instance, **kwargs):
    folioId = Recepcion.objects.get(folio=instance.folio)
    if not ResultadosTotal.objects.filter(folio_id=folioId).exists():
        cadena = verificadorCadena()
        ResultadosTotal.objects.create(
            slug = cadena,
            folio = folioId,
            folio_str = instance.folio,
            productor = instance.productor,
            organizacion = ex(Organizacion, instance.organizacion_id),
            fecha_recepcion = instance.fecha_recepcion,
            fecha_muestreo = instance.fecha_muestreo,
            tipo_analisis = ex(TipoAnalisis, instance.tipo_analisis_id),
            regimen_hidrico = ex(RegimenHidrico, instance.regimen_hidrico_id),
            profundida_cm = instance.profundida_cm,
            numero_hectareas = instance.numero_hectareas,
            cultivo_anterior = ex(Cultivo, instance.cultivo_anterior_id),
            cultivo_a_establecer = ex(Cultivo, instance.cultivo_a_establecer_id),
            rendimiento_esperado = instance.rendimiento_esperado,
            estado = ex(Estado, instance.estado_id),
            municipio = ex(Municipio, instance.municipio_id),
            localidad_ejido = instance.localidad_ejido,
            nombre_predio = instance.nombre_predio,
        )
    else:
        registro = ResultadosTotal.objects.get(folio_id=folioId)

        registro.folio_str = instance.folio
        registro.productor = instance.productor
        registro.organizacion = ex(Organizacion, instance.organizacion_id)
        registro.fecha_recepcion = instance.fecha_recepcion
        registro.fecha_muestreo = instance.fecha_muestreo
        registro.tipo_analisis = ex(TipoAnalisis, instance.tipo_analisis_id)
        registro.regimen_hidrico = ex(RegimenHidrico, instance.regimen_hidrico_id)
        registro.profundida_cm = instance.profundida_cm
        registro.numero_hectareas = instance.numero_hectareas
        registro.cultivo_anterior = ex(Cultivo, instance.cultivo_anterior_id)
        registro.cultivo_a_establecer = ex(Cultivo, instance.cultivo_a_establecer_id)
        registro.rendimiento_esperado = instance.rendimiento_esperado
        registro.estado = ex(Estado, instance.estado_id)
        registro.municipio = ex(Municipio, instance.municipio_id)
        registro.localidad_ejido = instance.localidad_ejido
        registro.nombre_predio = instance.nombre_predio
        registro.save()



@receiver(post_delete, sender=Recepcion)
def borrarFolio(sender, instance, **kwargs):
    folioId = instance.id
    ResultadosTotal.objects.filter(folio_id=folioId).delete()



# --- TEXTURA   
@receiver(post_save, sender=Textura)
def textura(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)
    
    #Actualizamos lo valores de Textura
    registro.textura_arenas = instance.arenas
    registro.textura_arcillas = instance.arcillas
    registro.textura_limos = instance.limos
    registro.textura_textura = instance.textura
    registro.save()


@receiver(post_delete, sender=Textura)
def borrarTextura(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.textura_arenas = None
    registro.textura_arcillas = None
    registro.textura_limos = None
    registro.textura_textura = None
    registro.save()



# --- PH Y CONDUCTIVIDAD ELECTRICA
@receiver(post_save, sender=Ph_ConductividadElectrica)
def phCe(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.ph = instance.ph
    registro.clasificacion_ph = instance.clasificacion_ph
    registro.ce = instance.ce
    registro.unidad = instance.unidad
    registro.clasificacion_ce = instance.clasificacion_ce
    registro.save()


@receiver(post_delete, sender=Ph_ConductividadElectrica)
def borrarPhCe(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.ph = None 
    registro.clasificacion_ph = None
    registro.ce = None
    registro.unidad = None
    registro.clasificacion_ce = None
    registro.save()


# --- MATERIA ORGANICA
@receiver(post_save, sender=MateriaOrganica)
def materiaOrganica(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.materia_organica = instance.materia_organica
    registro.interpretacionMO = instance.interpretacion
    registro.save()


@receiver(post_delete, sender=MateriaOrganica)
def borrarMateriaOrganica(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.materia_organica = None
    registro.interpretacionMO = None
    registro.save()


# --- COLOR Y DENSIDAD APARENTE
@receiver(post_save, sender=ColorDensidadAparente)
def colorDensidadAparente(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.clave_color = instance.clave
    registro.color = instance.color
    registro.densidad_aparente = instance.densidad_aparente
    registro.save()


@receiver(post_delete, sender=ColorDensidadAparente)
def borrarColorDensidadAparente(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.clave_color = None
    registro.color = None
    registro.densidad_aparente = None
    registro.save()


# --- PUNTO DE SATURACIÓN
@receiver(post_save, sender=PuntoSaturacion)
def puntoSaturacion(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.punto_saturacion =  instance.punto_saturacion
    registro.capacidad_campo =  instance.capacidad_campo
    registro.punto_marchitez =  instance.punto_marchitez
    registro.save()


@receiver(post_delete, sender=PuntoSaturacion)
def borrarPuntoSaturacion(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.punto_saturacion = None
    registro.capacidad_campo = None
    registro.punto_marchitez = None
    registro.save()



# --- NITROGENO
@receiver(post_save, sender=Nitrogeno)
def nitrogeno(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.nitrogeno = instance.nitrogeno
    registro.save()


@receiver(post_delete, sender=Nitrogeno)
def borrarNitrogeno(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.nitrogeno = None
    registro.save()



# --- CARBONATOS TOTALES
@receiver(post_save, sender=CarbonatosTotales)
def carbonatosTotales(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.CaCo3 = instance.CaCo3
    registro.save()


@receiver(post_delete, sender=CarbonatosTotales)
def borrarCarbonatosTotales(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.CaCo3 = None
    registro.save()



# --- MICRONUTRIENTES
@receiver(post_save, sender=Micronutrientes)
def micronutrientes(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.Fe = instance.Fe 
    registro.Cu = instance.Cu
    registro.Mn = instance.Mn
    registro.Zn = instance.Zn
    registro.save()


@receiver(post_delete, sender=Micronutrientes)
def borrarMicronutrientes(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.Fe = None 
    registro.Cu = None
    registro.Mn = None
    registro.Zn = None
    registro.save()



# --- BASES INTERCAMBIABLES
@receiver(post_save, sender=BasesIntercambiables)
def basesIntercambiables(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.Ca = instance.Ca
    registro.Mg = instance.Mg
    registro.Na = instance.Na
    registro.K = instance.K
    registro.save()


@receiver(post_delete, sender=BasesIntercambiables)
def borrarBasesIntercambiables(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.Ca = None
    registro.Mg = None
    registro.Na = None
    registro.K = None
    registro.save()



# --- FOSFORO
@receiver(post_save, sender=Fosforo)
def fosforo(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.tipo_fosforo = instance.tipo
    registro.fosforo = instance.fosforo
    registro.save()


@receiver(post_delete, sender=Fosforo)
def borrarFosforo(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.tipo_fosforo = None
    registro.fosforo = None
    registro.save()



# --- PH Y CONDUCTIVIDAD ELECTRICA PASTA SATURADA
@receiver(post_save, sender=PhCePasta)
def phCePasta(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.ph_pasta = instance.ph
    registro.ce_pasta = instance.ce
    registro.unidad_cePasta = instance.unidad
    registro.save()


@receiver(post_delete, sender=PhCePasta)
def borrarPhCePasta(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.ph_pasta = None
    registro.ce_pasta = None
    registro.unidad_cePasta = None
    registro.save()



# --- CATIONES
@receiver(post_save, sender=Cationes)
def cationes(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.CaCation = instance.CaCation
    registro.MgCation = instance.MgCation
    registro.NaCation = instance.NaCation
    registro.KCation = instance.KCation
    registro.save()


@receiver(post_delete, sender=Cationes)
def borrarCationes(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.CaCation = None
    registro.MgCation = None
    registro.NaCation = None
    registro.KCation = None
    registro.save()



# --- ANIONES
@receiver(post_save, sender=Aniones)
def aniones(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.carbonatos = instance.carbonatos
    registro.bicarbonatos = instance.bicarbonatos
    registro.cloruros = instance.cloruros
    registro.sulfatos = instance.sulfatos
    registro.save()
   

@receiver(post_delete, sender=Aniones)
def borrarAniones(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.carbonatos = None
    registro.bicarbonatos = None
    registro.cloruros = None
    registro.sulfatos = None
    registro.save()



# --- BASES DE CAMBIO
@receiver(post_save, sender=BasesCambio)
def basesCambio(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.CaMeq = instance.CaMeq
    registro.MgMeq = instance.MgMeq
    registro.NaMeq = instance.NaMeq
    registro.KMeq = instance.KMeq
    registro.Cic = instance.Cic
    registro.CaPorcentaje = instance.CaPorcentaje
    registro.MgPorcentaje = instance.MgPorcentaje
    registro.NaPorcentaje = instance.NaPorcentaje
    registro.KPorcentaje = instance.KPorcentaje
    registro.Ca_Mg = instance.Ca_Mg
    registro.Mg_K = instance.Mg_K
    registro.CaMg_K = instance.CaMg_K
    registro.Ca_K = instance.Ca_K
    registro.save()


@receiver(post_delete, sender=BasesCambio)
def borrarBasesCambio(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.CaMeq = None
    registro.MgMeq = None
    registro.NaMeq = None
    registro.KMeq = None
    registro.Cic = None
    registro.CaPorcentaje = None
    registro.MgPorcentaje = None
    registro.NaPorcentaje = None
    registro.KPorcentaje = None
    registro.Ca_Mg = None
    registro.Mg_K = None
    registro.CaMg_K = None
    registro.Ca_K = None
    registro.save()



# --- RAS Y PSI
@receiver(post_save, sender=RasPsi)
def rasPsi(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.Ras = instance.Ras
    registro.Psi = instance.Psi
    registro.save()


@receiver(post_delete, sender=RasPsi)
def borrarRasPsi(sender, instance, **kwargs):
    folioId = instance.folio
    registro = ResultadosTotal.objects.get(folio_id=folioId)

    registro.Ras = None
    registro.Psi = None
    registro.save()





def verificadorCadena():
    option = True
    
    while option:
       cadena = generadorCadenaConsulta()
       if not ResultadosTotal.objects.filter(slug=cadena).exists():
           option = False
           return cadena