from django.db import models
from analisis_nutrientes.models import BasesIntercambiables
from recepcion.models import Recepcion
from calculos.formula import basesCambio, rasPsi
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from analisis_salinidad.models import Cationes

# Create your models here.

class BasesCambio(models.Model):
    folio = models.OneToOneField(Recepcion, on_delete=models.CASCADE)
    CaMeq = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Ca+ (meq/100g)')
    MgMeq = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Mg++ (meq/100g)')
    NaMeq = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Na+ (meq/100g)')
    KMeq = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='K+ (meq/100g)')
    Cic = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Capacidad de Intercambio Cationico (CIC)')
    CaPorcentaje = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Ca+ (%)')
    MgPorcentaje = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Mg+ (%)')
    NaPorcentaje = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Na+ (%)')
    KPorcentaje = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='K+ (%)')
    Ca_Mg = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Ca/Mg')
    Mg_K = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Mg/K')
    CaMg_K = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='(Ca+Mg)/K')
    Ca_K = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Ca/K')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    def __str__(self):
        return str(self.folio)



class RasPsi(models.Model):
    folio = models.OneToOneField(Recepcion, on_delete=models.CASCADE)
    Ras = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='RAS')
    Psi = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='PSI')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    def __str__(self):
        return str(self.folio)


@receiver(post_save, sender=BasesIntercambiables)
def crearBasesCambio(sender, instance, **kwargs):
    folioId = instance.folio
        #Comprobamos que exista el folio en BasesIntercambiables
    if BasesIntercambiables.objects.filter(folio_id=folioId).exists():
        
        registroBasesIntercambiables = BasesIntercambiables.objects.get(folio_id = folioId)

        Cappm = registroBasesIntercambiables.Ca
        Mgppm = registroBasesIntercambiables.Mg
        Nappm = registroBasesIntercambiables.Na
        Kppm = registroBasesIntercambiables.K

        resultado = basesCambio(Cappm, Mgppm, Nappm, Kppm)
        #Comprobamos si el folio existe en Bases de Cambio, si es asi actualizamos, de lo contrario creamos
        if BasesCambio.objects.filter(folio_id=folioId).exists():
            registro = BasesCambio.objects.get(folio_id=folioId)
            
            registro.CaMeq = resultado['CaMeq'] 
            registro.MgMeq = resultado['MgMeq'] 
            registro.NaMeq = resultado['NaMeq'] 
            registro.KMeq = resultado['KMeq'] 
            registro.Cic = resultado['Cic'] 
            registro.CaPorcentaje = resultado['CaPorc'] 
            registro.MgPorcentaje = resultado['MgPorc'] 
            registro.NaPorcentaje = resultado['NaPorc'] 
            registro.KPorcentaje = resultado['KPorc'] 
            registro.Ca_Mg = resultado['Ca_Mg'] 
            registro.Mg_K = resultado['Mg_K'] 
            registro.CaMg_K = resultado['CaMg_K'] 
            registro.Ca_K = resultado['Ca_K']
            registro.save()

        else:

            BasesCambio.objects.create(
                folio = folioId,
                CaMeq = resultado['CaMeq'],
                MgMeq = resultado['MgMeq'], 
                NaMeq = resultado['NaMeq'], 
                KMeq = resultado['KMeq'], 
                Cic = resultado['Cic'], 
                CaPorcentaje = resultado['CaPorc'], 
                MgPorcentaje = resultado['MgPorc'], 
                NaPorcentaje = resultado['NaPorc'], 
                KPorcentaje = resultado['KPorc'], 
                Ca_Mg = resultado['Ca_Mg'], 
                Mg_K = resultado['Mg_K'], 
                CaMg_K = resultado['CaMg_K'], 
                Ca_K = resultado['Ca_K'], 
            )


@receiver(post_delete, sender=BasesIntercambiables)
def borrarBasesCambio(sender, instance, **kwargs):
    folioId = instance.folio
    BasesCambio.objects.filter(folio_id=folioId).delete()


@receiver(post_save, sender=BasesCambio)
def crearRasPsiBC(sender, instance, **kwargs):
    folioId = instance.folio
        #Comprobamos si el folio existe en Cationes y BasesCambio para poder realizar los calculos
    if Cationes.objects.filter(folio_id=folioId).exists() and BasesCambio.objects.filter(folio_id=folioId):
        registroCationes = Cationes.objects.get(folio_id =folioId)
        registroBasesCambio = BasesCambio.objects.get(folio_id=folioId)

        NaCat = registroCationes.NaCation
        CaCat = registroCationes.CaCation
        MgCat = registroCationes.MgCation
        Cic = registroBasesCambio.Cic

        resultado = rasPsi(NaCat, CaCat, MgCat, Cic)

        #Comprobamos si el folio existe en RasPsi, si es asi actualizamos, de lo contrario creamos
        if RasPsi.objects.filter(folio_id=folioId).exists():
            registro = RasPsi.objects.get(folio_id=folioId)

            registro.Ras = resultado['Ras'] 
            registro.Psi = resultado['Psi']
            registro.save()

        else:

            RasPsi.objects.create(
                folio = folioId,
                Ras = resultado['Ras'],
                Psi = resultado['Psi'],
            )


@receiver(post_save, sender=Cationes)
def crearRasPsiCat(sender, instance, **kwargs):
    folioId = instance.folio
        #Comprobamos si el folio existe en Cationes y BasesCambio para poder realizar los calculos
    if Cationes.objects.filter(folio_id=folioId).exists() and BasesCambio.objects.filter(folio_id=folioId):
        registroCationes = Cationes.objects.get(folio_id =folioId)
        registroBasesCambio = BasesCambio.objects.get(folio_id=folioId)

        NaCat = registroCationes.NaCation
        CaCat = registroCationes.CaCation
        MgCat = registroCationes.MgCation
        Cic = registroBasesCambio.Cic

        resultado = rasPsi(NaCat, CaCat, MgCat, Cic)

        #Comprobamos si el folio existe en RasPsi, si es asi actualizamos, de lo contrario creamos
        if RasPsi.objects.filter(folio_id=folioId).exists():
            registro = RasPsi.objects.get(folio_id=folioId)

            registro.Ras = resultado['Ras'] 
            registro.Psi = resultado['Psi']
            registro.save()

        else:

            RasPsi.objects.create(
                folio = folioId,
                Ras = resultado['Ras'],
                Psi = resultado['Psi'],
            )


@receiver(post_delete, sender=BasesCambio)
def borrarRasPsiBC(sender, instance, **kwargs):
    folioId = instance.folio
    if RasPsi.objects.filter(folio_id=folioId).exists():
        RasPsi.objects.filter(folio_id=folioId).delete()


@receiver(post_delete, sender=Cationes)
def borrarRasPsiCat(sender, instance, **kwargs):
    folioId = instance.folio
    if RasPsi.objects.filter(folio_id=folioId).exists():
        RasPsi.objects.filter(folio_id=folioId).delete()