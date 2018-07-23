from decimal import Decimal
import math
from analisis_nutrientes.models import BasesIntercambiables
from analisis_salinidad.models import Cationes
from recepcion.models import Recepcion
# from analisis_formula.models import BasesCambio, RasPsi



#---BASES DE CAMBIO CALCULAR
def basesCambio(Cappm, Mgppm, Nappm, Kppm):
    Cappm = Decimal(Cappm)
    Mgppm = Decimal(Mgppm)
    Nappm = Decimal(Nappm)
    Kppm = Decimal(Kppm)

    #Bases de Cambio en meq/100g
    CaMeq = Cappm / 200 
    MgMeq = Mgppm / 122
    NaMeq = Nappm / 391
    KMeq = Kppm / 230

    Cic = CaMeq + MgMeq + NaMeq + KMeq

    CaPorcentaje = (CaMeq / Cic) * 100 
    MgPorcentaje = (MgMeq / Cic) * 100
    NaPorcentaje = (NaMeq / Cic) * 100
    KPorcentaje = (KMeq / Cic) * 100

    # Relación de Bases de Cambio Ca/Mg, Mg/K, (Ca+Mg)/K, Ca/K
    Ca_Mg = CaMeq / MgMeq 
    Mg_K = MgMeq / KMeq
    CaMg_K = (CaMeq + MgMeq) / KMeq
    Ca_K = CaMeq / KMeq

    CaMeq = round(CaMeq, 2)
    MgMeq = round(MgMeq, 2)
    NaMeq = round(NaMeq, 2)
    KMeq = round(KMeq, 2)
    Cic = round(Cic, 2)
    CaPorcentaje = round(CaPorcentaje, 2) 
    MgPorcentaje = round(MgPorcentaje, 2)
    NaPorcentaje = round(NaPorcentaje, 2)
    KPorcentaje = round(KPorcentaje, 2)
    Ca_Mg = round(Ca_Mg, 2)
    Mg_K = round(Mg_K, 2)
    CaMg_K = round(CaMg_K, 2)
    Ca_K = round(Ca_K, 2)



    return {'CaMeq':CaMeq, 'MgMeq':MgMeq, 'NaMeq':NaMeq, 'KMeq':KMeq, 'CaPorc':CaPorcentaje, 'MgPorc':MgPorcentaje, 'NaPorc':NaPorcentaje, 'KPorc':KPorcentaje, 'Cic':Cic, 'Ca_Mg':Ca_Mg, 'Mg_K':Mg_K, 'CaMg_K':CaMg_K, 'Ca_K':Ca_K}


#---RAS Y PSI CALCULAR
def rasPsi(NaCat, CaCat, MgCat, Cic):
    NaCat = Decimal(NaCat)
    CaCat = Decimal(CaCat)
    MgCat = Decimal(MgCat)
    Cic = Decimal(Cic)

    Ras = NaCat / Decimal(math.sqrt((CaCat + MgCat)/2))
    Psi = (NaCat / Cic) * 100

    Ras = round(Ras, 2)
    Psi = round(Psi, 2)

    return {'Ras':Ras, 'Psi':Psi}



#---BASES DE CAMBIO CALCULAR A PARTIR DEL FOLIO
# def basesCambioFolio(folio):
#     registroRecepcion = Recepcion.objects.get(folio=folio)
#     registroBasesIntercambiables = BasesIntercambiables.objects.get(folio_id = registroRecepcion.id)
#     Cappm = registroBasesIntercambiables.Ca
#     Mgppm = registroBasesIntercambiables.Mg
#     Nappm = registroBasesIntercambiables.Na
#     Kppm = registroBasesIntercambiables.K

#     return basesCambio(Cappm, Mgppm, Nappm, Kppm)

    
   
# #---RAS Y PSI CALCULAR
# def rasPsiFolio(folio):
#     registroRecepcion = Recepcion.objects.get(folio=folio)
#     registroCationes = Cationes.objects.get(folio_id =registroRecepcion.id)
#     registroBasesCambio = BasesCambio.get(folio_id=registroRecepcion.id)

#     NaCat = registroCationes.Na
#     CaCat = registroCationes.Ca
#     MgCat = registroCationes.Mg
#     Cic = registroBasesCambio.Cic

#     return rasPsi(NaCat, CaCat, MgCat, Cic)


# #---BASES DE CAMBIO GUARDAR O ACTUALIZAR BASE DE DATOS
# def basesCambioGuardar(folio):
#     #Comprobamos que exista el folio en Recepcion
#     # if Recepcion.objects.filter(folio=folio).exists():
#     #     registroRecepcion = Recepcion.objects.get(folio=folio)
#     folioId = folio
#         #Comprobamos que exista el folio en BasesIntercambiables
#     if BasesIntercambiables.objects.filter(folio_id=folioId).exists():
#         resultado = basesCambioFolio(folio)
#         #Comprobamos si el folio existe en Bases de Cambio, si es asi actualizamos, de lo contrario creamos
#         if BasesCambio.objects.filter(folio_id=folioId).exists():
#             registro = BasesCambio.objects.get(folio_id=folioId)
            
#             registro.CaMeq = resultado['CaMeq'] 
#             registro.MgMeq = resultado['MgMeq'] 
#             registro.NaMeq = resultado['NaMeq'] 
#             registro.KMeq = resultado['KMeq'] 
#             registro.Cic = resultado['Cic'] 
#             registro.CaPorcentaje = resultado['CaPorc'] 
#             registro.MgPorcentaje = resultado['MgPorc'] 
#             registro.NaPorcentaje = resultado['NaPorc'] 
#             registro.KPorcentaje = resultado['KPorc'] 
#             registro.Ca_Mg = resultado['Ca_Mg'] 
#             registro.Mg_K = resultado['Mg_K'] 
#             registro.CaMg_K = resultado['CaMg_K'] 
#             registro.Ca_K = resultado['Ca_K']
#             registro.save()

#         else:

#             BasesCambio.objects.create(
#                 folio = folioId,
#                 CaMeq = resultado['CaMeq'],
#                 MgMeq = resultado['MgMeq'], 
#                 NaMeq = resultado['NaMeq'], 
#                 KMeq = resultado['KMeq'], 
#                 Cic = resultado['Cic'], 
#                 CaPorcentaje = resultado['CaPorc'], 
#                 MgPorcentaje = resultado['MgPorc'], 
#                 NaPorcentaje = resultado['NaPorc'], 
#                 KPorcentaje = resultado['KPorc'], 
#                 Ca_Mg = resultado['Ca_Mg'], 
#                 Mg_K = resultado['Mg_K'], 
#                 CaMg_K = resultado['CaMg_K'], 
#                 Ca_K = resultado['Ca_K'], 
#             )


# def rasPsiGuardar(folio):
#     #Comprobamos si exite el folio en recepción
#     if Recepcion.objects.filter(folio=folio).exists():
#         registroRecepcion = Recepcion.objects.get(folio=folio)
#         folioId = registroRecepcion.id
#         #Comprobamos si el folio existe en Cationes y BasesCambio para poder realizar los calculos
#         if Cationes.objects.filter(folio_id=folioId).exists() and BasesCambio.objects.filter(folio_id=folioId):
#             resultado = rasPsiFolio(folio)
#             #Comprobamos si el folio existe en RasPsi, si es asi actualizamos, de lo contrario creamos
#             if RasPsi.objects.filter(folio_id=folioId).exists():
#                 registro = RasPsi.objects.get(folio_id=folioId)

#                 registro.Ras = resultado['Ras'] 
#                 registro.Psi = resultado['Psi']
#                 registro.save()

#             else:

#                 RasPsi.objects.create(
#                     folio = folioId,
#                     Ras = resultado['Ras'],
#                     Psi = resultado['Psi'],
#                 )


