from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from django.views.generic import View, ListView
from django.views.generic.detail import DetailView
from .models import ResultadosTotal
from .forms import ConsulataForm

import datetime

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from calculos.reportes import (
    valor_str, valor_str_SD,
    clas_N, clas_P, clas_K, clas_Ca, clas_Mg, 
    clas_Na, clas_Fe, clas_Zn, clas_Mn, clas_Cu,
    clas_Ca_Mg, clas_Mg_K, clas_CaMg_K, clas_Ca_K,
    clas_Sales, clas_RAS,
    requerimiento_Nutrientes, ppm_kg_ha, aportacion_requerida,
)


# Create your views here.

class reporte_UsuariosPDF(View):
    form = ConsulataForm
    template_name = 'reportes/consulta_resultado.html'


    def cabecera(self,pdf):
        archivo_imagen = settings.MEDIA_ROOT+'/img/logo.png'
        pdf.drawImage(archivo_imagen, 520, 720, 56, 69, preserveAspectRatio=True)
        
    def titulo(self, pdf):
        #Estilo
        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 16)
        #pdf.setStrokeColorRGB(0.2,0.5,0.3)
        #pdf.setFillColorRGB(0,0,0.77)
        pdf.drawString(160, 750, 'Laboratorio Integral Agroalimentario')
        pdf.setFont('Helvetica', 13)
        pdf.drawString(165, 730, 'Resultados de Análisis Fisicoquimico de Suelo')

    def informacionGeneral(self, pdf, analisis):
        #estilo
        ancho_base = 30
        alto_base = 650
        inter = 25 #Interlineado
        inter_2 = 20

        ancho = ancho_base
        pdf.setFont('Helvetica-Bold', 11)
        pdf.drawString(ancho, alto_base+30 , 'INFORMACIÓN GENERAL')
        pdf.line(ancho, alto_base+28, 200, alto_base+28)
        #pdf.setFillColorRGB(1,0,1)
        

        
        #estilo
        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 10)

        alto = alto_base
        pdf.drawString(ancho, alto, 'Popietario:')
        pdf.drawString(ancho + 190, alto, 'No Registro:')
        pdf.drawString(ancho + 370, alto, 'Fecha de Recepción:')

        alto = alto-(inter*1)
        pdf.drawString(ancho, alto, 'Estado:')
        pdf.drawString(ancho + 160, alto, 'Municipio:')
        pdf.drawString(ancho + 300, alto, 'Ejido:')
        pdf.drawString(ancho + 430, alto, 'Predio:')

        alto = alto-(inter*1)
        pdf.drawString(ancho, alto, 'Cult. Anterior:')
        pdf.drawString(ancho + 130, alto, 'Cult. Sembrar:')
        pdf.drawString(ancho + 260, alto, 'Régimen Hum.:')
        pdf.drawString(ancho + 405, alto, 'Rendimiento Esperado:')
        

        #estilo
        pdf.setFont('Helvetica', 10)

        Productor = valor_str_SD(analisis.productor)
        Folio = valor_str_SD(analisis.folio_str)

        if analisis.fecha_recepcion == None:
            fecha = 'S.D.'
        else:
            fecha_R = analisis.fecha_recepcion
            fecha = fecha_R.strftime("%d/%m/%Y")

        
        Estado = valor_str_SD(analisis.estado)
        Municipio = valor_str_SD(analisis.municipio)
        Localidad = valor_str_SD(analisis.localidad_ejido)
        Predio = valor_str_SD(analisis.nombre_predio)
        Cultivo_Anterior = valor_str_SD(analisis.cultivo_anterior)
        Cultivo_Establecer = valor_str_SD(analisis.cultivo_a_establecer)
        Regimen_Hidrico = valor_str_SD(analisis.regimen_hidrico)
        rendimiento = valor_str_SD(analisis.rendimiento_esperado)

        alto_d = alto_base
        pdf.drawString(ancho + 55, alto_d, Productor)
        pdf.drawString(ancho+ 253, alto_d, Folio)
        
        
        pdf.drawString(ancho + 477, alto_d, fecha)

        alto_d = alto_d-(inter*1)
        pdf.drawString(ancho + 40, alto_d, Estado[:19])
        pdf.drawString(ancho + 213, alto_d, Municipio[:15])
        pdf.drawString(ancho + 330, alto_d, Localidad[:17])
        pdf.drawString(ancho+ 465, alto_d, Predio[:12])

        alto_d = alto_d-(inter*1)
        pdf.drawString(ancho + 67, alto_d, Cultivo_Anterior)
        pdf.drawString(ancho + 200, alto_d, Cultivo_Establecer)
        pdf.drawString(ancho + 333, alto_d, Regimen_Hidrico)
        
        pdf.drawString(ancho + 517, alto_d, rendimiento)


        ###CARACTERISTICAS DEL SUELO

        ## Titulo
        alto = alto - 30
        pdf.setStrokeColorRGB(1, 1, 1)
        pdf.setFillColorRGB(0, 0.3, 0)

        pdf.rect(ancho, alto-5, 550, 20, fill=1)

        pdf.setFillColorRGB(255, 255, 255)
        pdf.setFont('Helvetica-Bold', 11)
        pdf.drawString(ancho+200, alto , 'CARACTERISTICAS DEL SUELO')
        #pdf.line(ancho, alto-2, 200, alto-2)

        pdf.setFillColorRGB(0, 0, 0)
        pdf.setStrokeColorRGB(0, 0, 0)

        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 11)

        ## Encabezados
        alto = alto -20
        pdf.drawString(ancho, alto, 'Parametro')
        pdf.drawString(ancho + 150, alto, 'Resultado')
        pdf.drawString(ancho + 350, alto, 'Interpretación')
        pdf.line(ancho, alto-3, 580, alto-3)


        ## Parametros
        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 10)

        alto = alto -20
        pdf.drawString(ancho, alto, 'ph (1:2 Agua):')
        pdf.drawString(ancho, alto - inter_2, 'CE (1:2 Agua):')
        pdf.drawString(ancho, alto - (inter_2*2), 'CIC:')
        pdf.drawString(ancho, alto - (inter_2*3), 'Densidad Aparente:')
        pdf.drawString(ancho, alto - (inter_2*4), 'Materia Orgánica:')
        pdf.drawString(ancho, alto - (inter_2*5), 'Textura:')
        pdf.drawString(ancho, alto - (inter_2*6), 'Color:')
        pdf.drawString(ancho, alto - (inter_2*7), 'Punto de Saturación:')
        pdf.drawString(ancho, alto - (inter_2*8), 'Capacidad de Campo:')
        pdf.drawString(ancho, alto - (inter_2*9), 'PMP:')
        

        ## Valores
        
        pdf.setFont('Helvetica', 10)

        ph = valor_str(analisis.ph)
        ce = valor_str(analisis.ce)
        unidad_ce = valor_str(analisis.unidad)
        cic = valor_str(analisis.Cic)
        da = valor_str(analisis.densidad_aparente)
        mo = valor_str(analisis.materia_organica)
        tex_arenas = valor_str(analisis.textura_arenas)
        tex_arcillas = valor_str(analisis.textura_arcillas)
        tex_limos = valor_str(analisis.textura_limos)
        ps = valor_str(analisis.punto_saturacion)
        cc = valor_str(analisis.capacidad_campo)
        pmp = valor_str(analisis.punto_marchitez)
        color_clave = valor_str(analisis.clave_color).title()
        color_v = valor_str(analisis.color).title()
      


        alto_d = alto_d - 70

        pdf.drawString(ancho+150 , alto_d, ph)
        pdf.drawString(ancho+150 , alto_d - inter_2, ce + ' (' + unidad_ce + ')')
        pdf.drawString(ancho+150 , alto_d - (inter_2*2), cic)
        pdf.drawString(ancho+150 , alto_d - (inter_2*3), da + '(gr/cm3)')
        pdf.drawString(ancho+150 , alto_d - (inter_2*4), mo)
        pdf.setFont('Helvetica', 9)
        pdf.drawString(ancho+150 , alto_d - (inter_2*5), 'Arenas: ' + tex_arenas + ', Arcillas: ' + tex_arenas + ', Limos: ' + tex_limos)  
        pdf.setFont('Helvetica', 10)
        pdf.drawString(ancho+150 , alto_d - (inter_2*6), color_clave + ' ' + color_v)
        pdf.drawString(ancho+150 , alto_d - (inter_2*7), ps)
        pdf.drawString(ancho+150 , alto_d - (inter_2*8), cc)
        pdf.drawString(ancho+150 , alto_d - (inter_2*9), pmp)

        ## Interpretación
        pdf.drawString(ancho+350 , alto_d, valor_str(analisis.clasificacion_ph))
        pdf.drawString(ancho+350 , alto_d - inter_2, valor_str(analisis.clasificacion_ce).title())
        pdf.drawString(ancho+350 , alto_d - (inter_2*4), valor_str(analisis.interpretacionMO))
        pdf.drawString(ancho+350 , alto_d - (inter_2*5), valor_str(analisis.textura_textura).title())


        ### NUTRIENTES Y FERTILIDAD
        alto = alto - (inter_2*9) - 30
        pdf.setStrokeColorRGB(1, 1, 1)
        pdf.setFillColorRGB(0, 0.3, 0)

        pdf.rect(ancho, alto-5, 550, 20, fill=1)

        pdf.setFillColorRGB(255, 255, 255)
        pdf.setFont('Helvetica-Bold', 11)
        pdf.drawString(ancho+200, alto , 'NUTRIENTES Y FERTILIDAD DEL SUELO')
        #pdf.line(ancho, alto-2, 200, alto-2)

        pdf.setFillColorRGB(0, 0, 0)
        pdf.setStrokeColorRGB(0, 0, 0)

        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 7)

        ## Encabezados
        alto = alto -20
        pdf.drawString(ancho+7, alto, 'Determinación')
        pdf.drawString(ancho + 70, alto, 'Unidades')
        pdf.drawString(ancho + 125, alto, 'Resultado')

        # Rectangulos Encabezados Verticales
        pdf.rect(ancho, alto+15, 60, -230)
        pdf.rect(ancho+60, alto+15, 55, -230)
        pdf.rect(ancho+60+55, alto+15, 57, -230)

        # Rectagungulo para delimitar area
        pdf.rect(ancho+172,alto-5, 7*54, -210)

        # Rectangulo Encabezados Horizontal
        pdf.rect(ancho, alto-5, 60+55+57, 20)

        # Rectangulos de divisiones de Encabezados Escalas
        pdf.rect(ancho+172, alto-5, 378, 20)
        pdf.rect(ancho+172, alto-5, 54, 20)
        pdf.rect(ancho+226, alto-5, 54, 20)
        pdf.rect(ancho+280, alto-5, 54, 20)
        pdf.rect(ancho+334, alto-5, 54, 20)
        pdf.rect(ancho+388, alto-5, 54, 20)
        pdf.rect(ancho+442, alto-5, 54, 20)
        pdf.rect(ancho+496, alto-5, 54, 20)

        pdf.setFont('Helvetica', 7)

        # Encabezados de Escalas
        pdf.drawString(ancho+184, alto, 'Muy Bajo')
        pdf.drawString(ancho+226+15, alto, 'Bajo')
        pdf.drawString(ancho+280+15, alto, 'Mod. Bajo')
        pdf.drawString(ancho+334+15, alto, 'Mediano')
        pdf.drawString(ancho+388+15, alto, 'Mod. Alto')
        pdf.drawString(ancho+442+15, alto, 'Alto')
        pdf.drawString(ancho+496+15, alto, 'Muy Alto')


        # Nombre del Elemento
        pdf.setFont('Helvetica', 9)
        pdf.drawString(ancho+7, alto-inter_2, 'N-Inorg')
        pdf.drawString(ancho+7, alto-(inter_2*2), valor_str(analisis.tipo_fosforo))
        pdf.drawString(ancho+7, alto-(inter_2*3), 'K')
        pdf.drawString(ancho+7, alto-(inter_2*4), 'Ca')
        pdf.drawString(ancho+7, alto-(inter_2*5), 'Mg')
        pdf.drawString(ancho+7, alto-(inter_2*6), 'Na')
        pdf.drawString(ancho+7, alto-(inter_2*7), 'Fe')
        pdf.drawString(ancho+7, alto-(inter_2*8), 'Zn')
        pdf.drawString(ancho+7, alto-(inter_2*9), 'Mn')
        pdf.drawString(ancho+7, alto-(inter_2*10), 'Cu')
        #pdf.drawString(ancho+7, alto-(inter_2*11), 'B')
        #pdf.drawString(ancho+7, alto-(inter_2*12), 'P-Olsen')

        # Unidades
        pdf.drawString(ancho+73, alto-inter_2, '(ppm)')
        pdf.drawString(ancho+73, alto-(inter_2*2), '(ppm)')
        pdf.drawString(ancho+73, alto-(inter_2*3), '(ppm)')
        pdf.drawString(ancho+73, alto-(inter_2*4), '(ppm)')
        pdf.drawString(ancho+73, alto-(inter_2*5), '(ppm)')
        pdf.drawString(ancho+73, alto-(inter_2*6), '(ppm)')
        pdf.drawString(ancho+73, alto-(inter_2*7), '(ppm)')
        pdf.drawString(ancho+73, alto-(inter_2*8), '(ppm)')
        pdf.drawString(ancho+73, alto-(inter_2*9), '(ppm)')
        pdf.drawString(ancho+73, alto-(inter_2*10), '(ppm)')
        #pdf.drawString(ancho+73, alto-(inter_2*11), '(ppm)')
        #pdf.drawString(ancho+73, alto-(inter_2*12), '(ppm)')


        # Resultados de Nutrientes
        N = analisis.nitrogeno
        P = analisis.fosforo
        K = analisis.K
        Ca = analisis.Ca
        Mg = analisis.Mg
        Na = analisis.Na
        Fe = analisis.Fe
        Zn = analisis.Zn
        Mn = analisis.Mn
        Cu = analisis.Cu


        pdf.drawString(ancho+128, alto-inter_2, str(N))
        pdf.drawString(ancho+128, alto-(inter_2*2), str(P))
        pdf.drawString(ancho+128, alto-(inter_2*3), str(K))
        pdf.drawString(ancho+128, alto-(inter_2*4), str(Ca))
        pdf.drawString(ancho+128, alto-(inter_2*5), str(Mg))
        pdf.drawString(ancho+128, alto-(inter_2*6), str(Na))
        pdf.drawString(ancho+128, alto-(inter_2*7), str(Fe))
        pdf.drawString(ancho+128, alto-(inter_2*8), str(Zn))
        pdf.drawString(ancho+128, alto-(inter_2*9), str(Mn))
        pdf.drawString(ancho+128, alto-(inter_2*10), str(Cu))
        #pdf.drawString(ancho+128, alto-(inter_2*11), 'N.D')

        # **************************************************************
        # Datos para Graficas Elementos
        N_clas = clas_N(analisis.nitrogeno)
        P_clas = clas_P(analisis.fosforo, analisis.tipo_fosforo)
        K_clas = clas_K(analisis.K)
        Ca_clas = clas_Ca(analisis.Ca)
        Mg_clas = clas_Mg(analisis.Mg)
        Na_clas = clas_Na(analisis.Na)
        Fe_clas = clas_Fe(analisis.Fe)
        Zn_clas = clas_Zn(analisis.Zn)
        Mn_clas = clas_Mn(analisis.Mn)
        Cu_clas = clas_Cu(analisis.Cu)

        # Color del borde de las barras(graficas)
        pdf.setStrokeColorRGB(1, 1, 1)

        # Nitrogeno
        pdf.setFillColorRGB(.3765,.7882,.2196)
        pdf.rect(ancho+172, alto-inter_2+8, N_clas['valor'], -10, fill=1)
       
       # Fosforo
        pdf.setFillColorRGB(.302,.5882,.0353)
        pdf.rect(ancho+172, alto-(inter_2*2)+8, P_clas['valor'], -10, fill=1)

        # Potasio
        pdf.setFillColorRGB(.9294,.1961,.2118)
        pdf.rect(ancho+172, alto-(inter_2*3)+8, K_clas['valor'], -10, fill=1)

        #Calcio
        pdf.setFillColorRGB(.949,.6627,.3529)
        pdf.rect(ancho+172, alto-(inter_2*4)+8, Ca_clas['valor'], -10, fill=1)

        # Magnesio
        pdf.setFillColorRGB(.749,.4235,.0745)
        pdf.rect(ancho+172, alto-(inter_2*5)+8,  Mg_clas['valor'], -10, fill=1)

        # Sodio
        pdf.setFillColorRGB(.9804,.0275,.6471)
        pdf.rect(ancho+172, alto-(inter_2*6)+8, Na_clas['valor'], -10, fill=1)

        # Hierro
        pdf.setFillColorRGB(.7098,.8392,.80)
        pdf.rect(ancho+172, alto-(inter_2*7)+8, Fe_clas['valor'], -10, fill=1)

        # Zinc
        pdf.setFillColorRGB(.1725,.5216,.5216)
        pdf.rect(ancho+172, alto-(inter_2*8)+8, Zn_clas['valor'], -10, fill=1)

        # Manganeso
        pdf.setFillColorRGB(.0667,.1686,.8392)
        pdf.rect(ancho+172, alto-(inter_2*9)+8, Mn_clas['valor'], -10, fill=1)

        #Cobre
        pdf.setFillColorRGB(.0078,.6824,.749)
        pdf.rect(ancho+172, alto-(inter_2*10)+8, Cu_clas['valor'], -10, fill=1)

    def page_2(self, pdf):
        pdf.showPage()

        archivo_imagen = settings.MEDIA_ROOT+'/img/logo.png'
        pdf.drawImage(archivo_imagen, 520, 720, 56, 69, preserveAspectRatio=True)

        #Estilo
        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 16)
        #pdf.setStrokeColorRGB(0.2,0.5,0.3)
        #pdf.setFillColorRGB(0,0,0.77)
        pdf.drawString(160, 750, 'Laboratorio Integral Agroalimentario')
        pdf.setFont('Helvetica', 13)
        pdf.drawString(165, 730, 'Resultados de Análisis Fisicoquimico de Suelo')

    def bases_cambio(self, pdf, analisis):
        ancho_base = 30
        alto_base = 650
        inter = 25 #Interlineado
        inter_2 = 20

        ## Subtitulo
        alto = alto_base + 50
        ancho = ancho_base
        pdf.setStrokeColorRGB(1, 1, 1)
        pdf.setFillColorRGB(0, 0.3, 0)

        pdf.rect(ancho, alto-5, 550, 20, fill=1)

        pdf.setFillColorRGB(255, 255, 255)
        pdf.setFont('Helvetica-Bold', 11)
        pdf.drawString(ancho+100, alto , 'PORCENTAJE ACTUAL Y SUGERIDO DE LAS BASES DE CAMBIO')
        
        ### TABLA
        pdf.setFillColorRGB(0, 0, 0)
        pdf.setStrokeColorRGB(0, 0, 0)

        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 9)

        ## Encabezados
        alto = alto -20
        adicion_ancho = 55
        pdf.drawString(ancho+7, alto, 'Determinación')
        pdf.drawString(ancho + 90, alto, 'Unidades')
        pdf.drawString(ancho + 170, alto, 'H+')
        pdf.drawString(ancho + 170 + (adicion_ancho * 1), alto, 'Al++')
        pdf.drawString(ancho + 170 + (adicion_ancho * 2), alto, 'Ca++')
        pdf.drawString(ancho + 170 + (adicion_ancho * 3), alto, 'Mg++')
        pdf.drawString(ancho + 170 + (adicion_ancho * 4), alto, 'K++')
        pdf.drawString(ancho + 170 + (adicion_ancho * 5), alto, 'Na++')
        pdf.drawString(ancho + 170 + (adicion_ancho * 6), alto, 'CIC+')

        
        pdf.setFont('Helvetica', 9)

        alto = alto
        alto_rec = alto + 5
        
        # Determinación y Unidades
        pdf.drawString(ancho + 7, alto - (inter*2) / 1.25, 'Resultado')
        pdf.drawString(ancho + 90, alto - inter, 'meq/100gr')
        pdf.drawString(ancho + 90, alto - inter * 2, '% Actual')
        pdf.drawString(ancho + 7, alto - inter * 3, 'Sugerido')
        pdf.drawString(ancho + 90, alto - inter * 3, '% Sugerido')

        # Sugerido (Valores)
        pdf.drawString(ancho + 165, alto - inter * 3, '0 - 5')
        pdf.drawString(ancho + 165 + (adicion_ancho * 1), alto - inter * 3, '0 - 0.1')
        pdf.drawString(ancho + 165 + (adicion_ancho * 2), alto - inter * 3, '65 - 75')
        pdf.drawString(ancho + 165 + (adicion_ancho * 3), alto - inter * 3, '10 - 20')
        pdf.drawString(ancho + 165 + (adicion_ancho * 4), alto - inter * 3, '3 - 7')
        pdf.drawString(ancho + 165 + (adicion_ancho * 5), alto - inter * 3, '0 - 5')

        # Rectangulos para formar la tabla (Verticales)
        pdf.rect(ancho, alto_rec + 10, 75, -100)
        pdf.rect(ancho + 75, alto_rec+10, 75, -100)
        pdf.rect(ancho + 150, alto_rec+10, adicion_ancho, -100)
        pdf.rect(ancho + 150 + (adicion_ancho*1), alto_rec+10, adicion_ancho, -100)
        pdf.rect(ancho + 150 + (adicion_ancho*2), alto_rec+10, adicion_ancho, -100)
        pdf.rect(ancho + 150 + (adicion_ancho*3), alto_rec+10, adicion_ancho, -100)
        pdf.rect(ancho + 150 + (adicion_ancho*4), alto_rec+10, adicion_ancho, -100)
        pdf.rect(ancho + 150 + (adicion_ancho*5), alto_rec+10, adicion_ancho, -100)
        pdf.rect(ancho + 150 + (adicion_ancho*6), alto_rec+10, 70, -100)

        # Rectangulos para formar la tabla (Horizontales)
        pdf.rect(ancho, alto_rec + 10 - inter, 75, - (inter * 2)) # Resultado

        pdf.rect(ancho, alto_rec+10, 550, -inter)
        pdf.rect(ancho + 75, alto_rec+10-(inter*1),75 + (adicion_ancho*6), -inter)
        pdf.rect(ancho + 75, alto_rec+10-(inter*2),75 + (adicion_ancho*6), -inter)
        pdf.rect(ancho + 75, alto_rec+10-(inter*3),75 + (adicion_ancho*6), -inter)

        ## OBTENCIÓN DE VALORES
        CaMeq = valor_str(analisis.CaMeq)
        MgMeq = valor_str(analisis.MgMeq)
        NaMeq = valor_str(analisis.NaMeq)
        KMeq = valor_str(analisis.KMeq)
        Cic = valor_str(analisis.Cic)
        CaPorcentaje = valor_str(analisis.CaPorcentaje)
        MgPorcentaje = valor_str(analisis.MgPorcentaje)
        NaPorcentaje = valor_str(analisis.NaPorcentaje)
        KPorcentaje = valor_str(analisis.KPorcentaje)

        # Impresión de Valores
        # H+
        pdf.drawString(ancho + 165, alto - (inter * 1), 'N.D.')
        pdf.drawString(ancho + 165, alto - (inter * 2), 'N.D.')
        # Al++
        pdf.drawString(ancho + 165 + (adicion_ancho * 1), alto - (inter * 1), 'N.D.')
        pdf.drawString(ancho + 165 + (adicion_ancho * 1), alto - (inter * 2), 'N.D.')
        # Ca++
        pdf.drawString(ancho + 165 + (adicion_ancho * 2), alto - (inter * 1), CaMeq)
        pdf.drawString(ancho + 165 + (adicion_ancho * 2), alto - (inter * 2), CaPorcentaje)
        # Mg++
        pdf.drawString(ancho + 165 + (adicion_ancho * 3), alto - (inter * 1), MgMeq)
        pdf.drawString(ancho + 165 + (adicion_ancho * 3), alto - (inter * 2), MgPorcentaje)
        # Mg++
        pdf.drawString(ancho + 165 + (adicion_ancho * 4), alto - (inter * 1), KMeq)
        pdf.drawString(ancho + 165 + (adicion_ancho * 4), alto - (inter * 2), KPorcentaje)
        # Na++
        pdf.drawString(ancho + 165 + (adicion_ancho * 5), alto - (inter * 1), NaMeq)
        pdf.drawString(ancho + 165 + (adicion_ancho * 5), alto - (inter * 2), NaPorcentaje)
        # CIC
        pdf.drawString(ancho + 165 + (adicion_ancho * 6), alto - (inter * 2), Cic)

    def rel_bases_cambio(self, pdf, analisis):
        ancho = 30
        alto = 650 - (25*4)
        inter = 25 #Interlineado
        inter_grafi = 30
        inter_2 = 20
       
       ## Subtitulo 1
        pdf.setStrokeColorRGB(1, 1, 1)
        pdf.setFillColorRGB(0, 0.3, 0)

        pdf.rect(ancho, alto-5, 250, 20, fill=1)

        pdf.setFillColorRGB(255, 255, 255)
        pdf.setFont('Helvetica-Bold', 11)
        pdf.drawString(ancho+40, alto , 'RELACIÓN DE BASES DE CAMBIO')

         ## Subtitulo 2
        pdf.setStrokeColorRGB(1, 1, 1)
        pdf.setFillColorRGB(0, 0.3, 0)

        pdf.rect(ancho + 260 , alto-5, 290, 20, fill=1)

        pdf.setFillColorRGB(255, 255, 255)
        pdf.setFont('Helvetica-Bold', 11)
        pdf.drawString(ancho+305, alto , 'EXTRACTO DE SALINIDAD Y SODICIDAD')

        ## Grafico
        pdf.setFillColorRGB(0, 0, 0)
        pdf.setStrokeColorRGB(0, 0, 0)

        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 9)

        alto = alto - inter_grafi
        ancho_txt = ancho + 10
        pdf.drawString(ancho_txt, alto, 'Muy Alto')
        pdf.drawString(ancho_txt, alto- (inter_grafi * 1), 'Alto')
        pdf.drawString(ancho_txt, alto- (inter_grafi * 2), 'Mediano')
        pdf.drawString(ancho_txt, alto- (inter_grafi * 3), 'Bajo')
        pdf.drawString(ancho_txt, alto- (inter_grafi * 4), 'Muy Bajo')

        ## Rectangulo grafico
        y_rec = alto + 17
        largo_rec = 65
        ancho_rec = 30
        pdf.rect(ancho, y_rec, largo_rec, -ancho_rec)
        pdf.rect(ancho, y_rec - (ancho_rec * 1), largo_rec, -ancho_rec)
        pdf.rect(ancho, y_rec - (ancho_rec * 2), largo_rec, -ancho_rec)
        pdf.rect(ancho, y_rec - (ancho_rec * 3), largo_rec, -ancho_rec)
        pdf.rect(ancho, y_rec - (ancho_rec * 4), largo_rec, -ancho_rec)

        ## TABLA INFERIOR DEL GRAFICO
        #Texto
        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 8)

        alto_txt_tabla = alto -(inter_grafi * 5)
        ancho_txt_tabla = ancho + 10
        y_txt_vertical = alto_txt_tabla + 5
        #Encabezados Verticales
        pdf.drawString(ancho_txt_tabla, y_txt_vertical, 'Relación')
        pdf.drawString(ancho_txt_tabla, y_txt_vertical - (inter_2 * 1), 'Resultado')
        pdf.drawString(ancho_txt_tabla, y_txt_vertical - (inter_2 * 2), 'Rango Medio')

        # Encabezados Horizontales
        pdf.setFont('Helvetica-Bold', 7)
        ancho_in_enc_ho = ancho + largo_rec + 15
        ancho_text_ho = 45
        pdf.drawString(ancho_in_enc_ho, y_txt_vertical, 'Ca/Mg')
        pdf.drawString(ancho_in_enc_ho + (ancho_text_ho * 1), y_txt_vertical, 'Mg/K')
        pdf.drawString(ancho_in_enc_ho-5 + (ancho_text_ho * 2), y_txt_vertical, 'Ca+Mg/K')
        pdf.drawString(ancho_in_enc_ho + (ancho_text_ho * 3), y_txt_vertical, 'Ca/K')

        # Rectangulos Verticales
        y_rec = alto_txt_tabla + 17
        largo_rec = ancho_text_ho
        ancho_rec = (inter_2 * 3)
        pdf.rect(ancho, y_rec, 65, -ancho_rec)
        # pdf.rect(ancho + 75, y_rec, largo_rec, -ancho_rec)
        # pdf.rect(ancho + 75 + (largo_rec * 1), y_rec, largo_rec, -ancho_rec)
        # pdf.rect(ancho + 75 + (largo_rec * 2), y_rec, largo_rec, -ancho_rec)
        # pdf.rect(ancho + 75 + (largo_rec * 3), y_rec, largo_rec, -ancho_rec)

        # Rectangulo Horizontal Unico
        pdf.rect(ancho, y_rec - (inter_2 * 0), 60 + (largo_rec * 4), -20)
        pdf.rect(ancho, y_rec - (inter_2 * 1), 60 + (largo_rec * 4), -20)

        # Rectangulo que enmarca la grafica
        pdf.rect(ancho, alto+17, 240, -150-(inter_2*3))

        # Obtención de valores y resultados
        Ca_Mg = valor_str(analisis.Ca_Mg)
        Mg_K = valor_str(analisis.Mg_K)
        CaMg_K = valor_str(analisis.CaMg_K)
        Ca_K = valor_str(analisis.Ca_K)

        # Impresión de valores en la tabla
        x_val = ancho + 80
        y_val = y_txt_vertical - inter_2
        x_aum = ancho_text_ho

        pdf.drawString(x_val, y_val, Ca_Mg)
        pdf.drawString(x_val + (x_aum * 1), y_val, Mg_K)
        pdf.drawString(x_val + (x_aum * 2), y_val, CaMg_K)
        pdf.drawString(x_val + (x_aum * 3), y_val, Ca_K)

        # Impresión de Rango Medio
        pdf.drawString(x_val, y_val - inter_2, "2 - 6")
        pdf.drawString(x_val + (x_aum * 1), y_val - inter_2, "2 - 3")
        pdf.drawString(x_val + (x_aum * 2), y_val - inter_2, "20 - 30")
        pdf.drawString(x_val + (x_aum * 3), y_val - inter_2, "10 - 15")

        # Gaficar Resultados

            ## Obtención de resultados clasificación
        Ca_Mg_class = clas_Ca_Mg(analisis.Ca_Mg)
        Mg_K_class = clas_Ca_Mg(analisis.Mg_K)
        CaMg_K_class = clas_Ca_Mg(analisis.CaMg_K)
        Ca_K_class = clas_Ca_Mg(analisis.Ca_K)

        pdf.setStrokeColorRGB(1, 1, 1)
        pdf.setFillColorRGB(.0039,.7020,.9922)

        #Rectangulo (inicio en x, inicio en Y, Largo, Ancho)
        base_x = x_val+3
        base_y = y_txt_vertical + 12
        largo_graf = 12
        aumento_x = 45
        escala_base = 30
        pdf.rect(base_x, base_y, largo_graf, Ca_Mg_class['valor'], fill=1)
        pdf.rect(base_x + (aumento_x * 1), base_y, largo_graf, Mg_K_class['valor'], fill=1)
        pdf.rect(base_x + (aumento_x * 2), base_y, largo_graf, CaMg_K_class['valor'], fill=1)
        pdf.rect(base_x + (aumento_x * 3), base_y, largo_graf, Ca_K_class['valor'], fill=1)
        

    def extracto_salinidad(self, pdf, analisis):
        base_x = 290
        base_y = 520
        inter = 20

        ## OBTENCIÓN DE RESULTADOS
        ph_pasta = valor_str(analisis.ph_pasta)
        ce_pasta = valor_str(analisis.ce_pasta)
        unidad_cePasta = valor_str(analisis.unidad_cePasta)
        Ras = valor_str(analisis.Ras)
        Psi = valor_str(analisis.Psi)
        CaCation = valor_str(analisis.CaCation)
        MgCation = valor_str(analisis.MgCation)
        NaCation = valor_str(analisis.NaCation)
        KCation = valor_str(analisis.KCation)
        carbonatos = valor_str(analisis.carbonatos)
        bicarbonatos = valor_str(analisis.bicarbonatos)
        cloruros = valor_str(analisis.cloruros)
        sulfatos = valor_str(analisis.sulfatos)



        pdf.setFillColorRGB(0, 0, 0)
        pdf.setStrokeColorRGB(0, 0, 0)

        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 8)

        # Concepto Parte Superior
        txt_x = base_x + 10
        txt_y = base_y
        incre_x = 90
        pdf.drawString(txt_x, txt_y, "Cee")
        pdf.drawString(txt_x, txt_y - inter, "pHe")
        pdf.drawString(txt_x + incre_x, txt_y, "RAS")
        pdf.drawString(txt_x + incre_x, txt_y - inter, "PSI")

        #Resultados Parte Superior
        txt_x2 = txt_x + 25
        pdf.setFont('Helvetica', 8)
        pdf.drawString(txt_x2, txt_y, ce_pasta + "( "+ unidad_cePasta +")")
        pdf.drawString(txt_x2, txt_y - inter, ph_pasta)
        pdf.drawString(txt_x2 + incre_x, txt_y, Ras)
        pdf.drawString(txt_x2 + incre_x, txt_y - inter, Psi)


        #Encabezado Segundo cuadro
        pdf.setFont('Helvetica-Bold', 10)
        txt_y2 = txt_y - (inter * 3)
        txt_x_b = base_x + 5
        pdf.drawString(txt_x_b, txt_y2, "Cationes (Meq/l)")
        pdf.drawString(txt_x_b + incre_x, txt_y2, "Aniones (Meq/l)")

        # Conceptos Parte Inferior
        pdf.setFont('Helvetica-Bold', 8)
        txt_y3 = txt_y2 - inter 
            # Cationes  
        pdf.drawString(txt_x, txt_y3, "Ca++")
        pdf.drawString(txt_x, txt_y3 - (inter * 1), "Mg++")
        pdf.drawString(txt_x, txt_y3 - (inter * 2), "Na+")
        pdf.drawString(txt_x, txt_y3 - (inter * 3), "K+")
        pdf.drawString(txt_x, txt_y3 - (inter * 4), "PO4")

            # Aniones  
        pdf.drawString(txt_x + incre_x, txt_y3, "CO3")
        pdf.drawString(txt_x + incre_x, txt_y3 - (inter * 1), "HCO3")
        pdf.drawString(txt_x + incre_x, txt_y3 - (inter * 2), "Cl-")
        pdf.drawString(txt_x + incre_x, txt_y3 - (inter * 3), "SO4")
        pdf.drawString(txt_x + incre_x, txt_y3 - (inter * 4), "N-NO3")

       #Resultados Parte Inferior
        txt_x3 = txt_x + 30
        pdf.setFont('Helvetica', 8)
            # Cationes  
        pdf.drawString(txt_x3, txt_y3, CaCation)
        pdf.drawString(txt_x3, txt_y3 - (inter * 1), MgCation)
        pdf.drawString(txt_x3, txt_y3 - (inter * 2), NaCation)
        pdf.drawString(txt_x3, txt_y3 - (inter * 3), KCation)
        pdf.drawString(txt_x3, txt_y3 - (inter * 4), "N.D.")
        
            # Aniones  
        pdf.drawString(txt_x3 + incre_x, txt_y3, carbonatos)
        pdf.drawString(txt_x3 + incre_x, txt_y3 - (inter * 1), bicarbonatos)
        pdf.drawString(txt_x3 + incre_x, txt_y3 - (inter * 2), cloruros)
        pdf.drawString(txt_x3 + incre_x, txt_y3 - (inter * 3), sulfatos)
        pdf.drawString(txt_x3 + incre_x, txt_y3 - (inter * 4), "N.D.")

        ## Rectangulo Tabla
        rec_tabla_y = base_y + 17
        rec_tabla_x = base_x
        pdf.rect(rec_tabla_x, rec_tabla_y, 172, -190)


        ###GRAFICO
        graf_x = txt_x3 + 140
        graf_y = base_y
        graf_inter = 30

        pdf.setFont('Helvetica-Bold', 8)
        pdf.drawString(graf_x, graf_y, 'Muy Alto')
        pdf.drawString(graf_x, graf_y - (graf_inter * 1), 'Alto')
        pdf.drawString(graf_x, graf_y - (graf_inter * 2), 'Mod. Alto')
        pdf.drawString(graf_x, graf_y - (graf_inter * 3), 'Mediano')
        pdf.drawString(graf_x, graf_y - (graf_inter * 4), 'Mod. Bajo')
        pdf.drawString(graf_x, graf_y - (graf_inter * 5), 'Bajo')
        pdf.drawString(graf_x, graf_y - (graf_inter * 6), 'Muy Bajo')

        ## Rectangulo Grafico
        rec_graf_y = graf_y + 17
        rec_graf_x = graf_x - 5
        pdf.rect(rec_graf_x, rec_graf_y, 115, -210)

        ## Rectangulos Escalas de Valores
        alto_rec = graf_inter
        largo_rec = 45
        
        pdf.rect(rec_graf_x, rec_graf_y, largo_rec, -alto_rec)
        pdf.rect(rec_graf_x, rec_graf_y - (alto_rec * 1), largo_rec, -alto_rec)
        pdf.rect(rec_graf_x, rec_graf_y - (alto_rec * 2), largo_rec, -alto_rec)
        pdf.rect(rec_graf_x, rec_graf_y - (alto_rec * 3), largo_rec, -alto_rec)
        pdf.rect(rec_graf_x, rec_graf_y - (alto_rec * 4), largo_rec, -alto_rec)
        pdf.rect(rec_graf_x, rec_graf_y - (alto_rec * 5), largo_rec, -alto_rec)
        pdf.rect(rec_graf_x, rec_graf_y - (alto_rec * 6), largo_rec, -alto_rec)

        # Texto Base de Grafica
        txt_base_graf_x = graf_x
        txt_base_graf_y = graf_y - 205
        incre_x_b = 47

        pdf.drawString(txt_base_graf_x, txt_base_graf_y, 'Grado de')
        pdf.setFont('Helvetica', 8)
        pdf.drawString(txt_base_graf_x + (incre_x_b * 1), txt_base_graf_y, 'Sales')
        pdf.drawString(txt_base_graf_x + (incre_x_b * 2)-7, txt_base_graf_y, 'RAS')

        # Gaficar Resultados
        pdf.setStrokeColorRGB(1, 1, 1)
        pdf.setFillColorRGB(.0039,.7020,.9922)

                    #Rectangulo (inicio en x, inicio en Y, Largo, Ancho)

        ## Valores para grafico 
        sales_clas = clas_Sales(analisis.NaCation)
        rass_clas = clas_RAS(analisis.Ras)

        base_x = txt_base_graf_x + 50
        base_y = txt_base_graf_y + 12
        largo_graf = 12
        aumento_x = 40
        escala_base = alto_rec
        pdf.rect(base_x, base_y, largo_graf, sales_clas['valor'], fill=1)
        pdf.rect(base_x + (aumento_x * 1), base_y, largo_graf, rass_clas['valor'], fill=1)
        

    def aportacion_requ(self, pdf, analisis):
        base_x = 30
        base_y = 280
        inter = 20
        

        ## Encabezado Principal
        pdf.setStrokeColorRGB(1, 1, 1)
        pdf.setFillColorRGB(0, 0.3, 0)

        pdf.rect(base_x, base_y, 550, 20, fill=1)

        pdf.setFillColorRGB(255, 255, 255)
        pdf.setFont('Helvetica-Bold', 14)
        pdf.drawString(base_x+70, base_y+5 , 'Requerimientos, Aportación y Necesidades de Nutrientes')

        #Subtitulos
        pdf.setFillColorRGB(0, 0, 0)
        pdf.setStrokeColorRGB(0, 0, 0)

        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 10)

        subtitulo_x = base_x + 120
        pdf.drawString(subtitulo_x, base_y - inter, "Necesidades de Nutrientes para el Rendimiento Esperado (kg/ha)")
        pdf.drawString(subtitulo_x + 50, base_y - inter * 5, "Nutrientes Existentes en el Suelo  (kg/ha)")
        pdf.drawString(subtitulo_x + 50, base_y - inter * 8, "Aportación Requerida (kg/ha)")

        #Subtitulos Elementos
        elemento_x = base_x + 10
        incremento_x = 40
        pdf.drawString(elemento_x, base_y - (inter * 2), "N")
        pdf.drawString(elemento_x +(incremento_x * 1), base_y - (inter * 2), "P")
        pdf.drawString(elemento_x +(incremento_x * 2), base_y - (inter * 2), "K")
        pdf.drawString(elemento_x +(incremento_x * 3), base_y - (inter * 2), "Ca")
        pdf.drawString(elemento_x +(incremento_x * 4), base_y - (inter * 2), "Mg")
        pdf.drawString(elemento_x +(incremento_x * 5), base_y - (inter * 2), "S")
        pdf.drawString(elemento_x +(incremento_x * 6), base_y - (inter * 2), "B")
        pdf.drawString(elemento_x +(incremento_x * 7), base_y - (inter * 2), "Cl")
        pdf.drawString(elemento_x +(incremento_x * 8), base_y - (inter * 2), "Cu")
        pdf.drawString(elemento_x +(incremento_x * 9), base_y - (inter * 2), "Fe")
        pdf.drawString(elemento_x +(incremento_x * 10), base_y - (inter * 2), "Mn")
        pdf.drawString(elemento_x +(incremento_x * 11), base_y - (inter * 2), "Mo")
        pdf.drawString(elemento_x +(incremento_x * 12), base_y - (inter * 2), "Zn")
        pdf.drawString(elemento_x +(incremento_x * 13), base_y - (inter * 2), "Ni")

        # Valores Necesidades
        necesidades = requerimiento_Nutrientes(analisis.cultivo_a_establecer, analisis.rendimiento_esperado)
        
        # Valores Kg Existentes
        N_e = ppm_kg_ha(analisis.nitrogeno, 30, analisis.densidad_aparente) 
        P_e = ppm_kg_ha(analisis.fosforo, 30, analisis.densidad_aparente) 
        K_e = ppm_kg_ha(analisis.K, 30, analisis.densidad_aparente) 
        Ca_e = ppm_kg_ha(analisis.Ca, 30, analisis.densidad_aparente) 
        Mg_e = ppm_kg_ha(analisis.Mg, 30, analisis.densidad_aparente) 
        S_e = "N.D." 
        B_e = "N.D." 
        Cl_e = "N.D." 
        Cu_e = ppm_kg_ha(analisis.Cu, 30, analisis.densidad_aparente) 
        Fe_e = ppm_kg_ha(analisis.Fe, 30, analisis.densidad_aparente) 
        Mn_e = ppm_kg_ha(analisis.Mn, 30, analisis.densidad_aparente) 
        Mo_e = "N.D." 
        Zn_e = ppm_kg_ha(analisis.Zn, 30, analisis.densidad_aparente) 
        Ni_e = "N.D."

        # Valores Aportación Requerida
        N_a = aportacion_requerida(analisis.nitrogeno, 'N', analisis.cultivo_a_establecer, analisis.rendimiento_esperado, 30, analisis.densidad_aparente)
        P_a = aportacion_requerida(analisis.fosforo, 'P', analisis.cultivo_a_establecer, analisis.rendimiento_esperado, 30, analisis.densidad_aparente)
        K_a = aportacion_requerida(analisis.K, 'K', analisis.cultivo_a_establecer, analisis.rendimiento_esperado, 30, analisis.densidad_aparente)
        Ca_a = aportacion_requerida(analisis.Ca, 'Ca', analisis.cultivo_a_establecer, analisis.rendimiento_esperado, 30, analisis.densidad_aparente)
        Mg_a = aportacion_requerida(analisis.Mg, 'Mg', analisis.cultivo_a_establecer, analisis.rendimiento_esperado, 30, analisis.densidad_aparente)
        S_a = "N.D."
        B_a = "N.D."
        Cl_a = "N.D."
        Cu_a = aportacion_requerida(analisis.Cu, 'Cu', analisis.cultivo_a_establecer, analisis.rendimiento_esperado, 30, analisis.densidad_aparente)
        Fe_a = aportacion_requerida(analisis.Fe, 'Fe', analisis.cultivo_a_establecer, analisis.rendimiento_esperado, 30, analisis.densidad_aparente)
        Mn_a = aportacion_requerida(analisis.Mn, 'Mn', analisis.cultivo_a_establecer, analisis.rendimiento_esperado, 30, analisis.densidad_aparente)
        Mo_a = "N.D."
        Zn_a = aportacion_requerida(analisis.Zn, 'Zn', analisis.cultivo_a_establecer, analisis.rendimiento_esperado, 30, analisis.densidad_aparente)
        Ni_a = "N.D."

        # Impresión de valores necesidades
        pdf.setFont('Helvetica', 8)
        res_x = base_x + 5
        res_y = base_y - (inter * 3)
        pdf.drawString(res_x, res_y, str(necesidades['N']))
        pdf.drawString(res_x + (incremento_x * 1), res_y, str(necesidades['P']))
        pdf.drawString(res_x + (incremento_x * 2), res_y, str(necesidades['K']))
        pdf.drawString(res_x + (incremento_x * 3), res_y, str(necesidades['Ca']))
        pdf.drawString(res_x + (incremento_x * 4), res_y, str(necesidades['Mg']))
        pdf.drawString(res_x + (incremento_x * 5), res_y, str(necesidades['S']))
        pdf.drawString(res_x + (incremento_x * 6), res_y, str(necesidades['B']))
        pdf.drawString(res_x + (incremento_x * 7), res_y, str(necesidades['Cl']))
        pdf.drawString(res_x + (incremento_x * 8), res_y, str(necesidades['Cu']))
        pdf.drawString(res_x + (incremento_x * 9), res_y, str(necesidades['Fe']))
        pdf.drawString(res_x + (incremento_x * 10), res_y, str(necesidades['Mn']))
        pdf.drawString(res_x + (incremento_x * 11), res_y, str(necesidades['Mo']))
        pdf.drawString(res_x + (incremento_x * 12), res_y, str(necesidades['Zn']))
        pdf.drawString(res_x + (incremento_x * 13), res_y, str(necesidades['Ni']))

        # Impresión de valores Kg/Ha Existentes
        
        res_y2 = base_y - (inter * 6)
        pdf.drawString(res_x, res_y2, str(N_e))
        pdf.drawString(res_x + (incremento_x * 1), res_y2, str(P_e))
        pdf.drawString(res_x + (incremento_x * 2), res_y2, str(K_e))
        pdf.drawString(res_x + (incremento_x * 3), res_y2, str(Ca_e))
        pdf.drawString(res_x + (incremento_x * 4), res_y2, str(Mg_e))
        pdf.drawString(res_x + (incremento_x * 5), res_y2, str(S_e))
        pdf.drawString(res_x + (incremento_x * 6), res_y2, str(B_e))
        pdf.drawString(res_x + (incremento_x * 7), res_y2, str(Cl_e))
        pdf.drawString(res_x + (incremento_x * 8), res_y2, str(Cu_e))
        pdf.drawString(res_x + (incremento_x * 9), res_y2, str(Fe_e))
        pdf.drawString(res_x + (incremento_x * 10), res_y2, str(Mn_e))
        pdf.drawString(res_x + (incremento_x * 11), res_y2, str(Mo_e))
        pdf.drawString(res_x + (incremento_x * 12), res_y2, str(Zn_e))
        pdf.drawString(res_x + (incremento_x * 13), res_y2, str(Ni_e))

        # Impresión de valores Kg/Ha Existentes
        
        res_y3 = base_y - (inter * 9)
        pdf.drawString(res_x, res_y3, str(N_a))
        pdf.drawString(res_x + (incremento_x * 1), res_y3, str(P_a))
        pdf.drawString(res_x + (incremento_x * 2), res_y3, str(K_a))
        pdf.drawString(res_x + (incremento_x * 3), res_y3, str(Ca_a))
        pdf.drawString(res_x + (incremento_x * 4), res_y3, str(Mg_a))
        pdf.drawString(res_x + (incremento_x * 5), res_y3, str(S_a))
        pdf.drawString(res_x + (incremento_x * 6), res_y3, str(B_a))
        pdf.drawString(res_x + (incremento_x * 7), res_y3, str(Cl_a))
        pdf.drawString(res_x + (incremento_x * 8), res_y3, str(Cu_a))
        pdf.drawString(res_x + (incremento_x * 9), res_y3, str(Fe_a))
        pdf.drawString(res_x + (incremento_x * 10), res_y3, str(Mn_a))
        pdf.drawString(res_x + (incremento_x * 11), res_y3, str(Mo_a))
        pdf.drawString(res_x + (incremento_x * 12), res_y3, str(Zn_a))
        pdf.drawString(res_x + (incremento_x * 13), res_y3, str(Ni_a))

        # Rectangulos
        rec_x = base_x
        rec_y = base_y
        pdf.rect(rec_x, rec_y,550, -(inter*10))

        # Indicacion de N.D.
        pdf.drawString(res_x, res_y3-30, "*N.D. ==> No Determinado")

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form})


    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        
        if form.is_valid():
            clave = form.cleaned_data['clave_consulta']

            if ResultadosTotal.objects.filter(slug=clave).exists():
                analisis = ResultadosTotal.objects.get(slug=clave)

                response = HttpResponse(content_type='application/pdf')
                # Para descargar el pdf con un nombre especifico
                #response['Content-Disposition'] = 'attachment; filename=prueba-lab.pdf'
                buffer = BytesIO()
                pdf = canvas.Canvas(buffer, pagesize=letter)

                self.cabecera(pdf)
                self.titulo(pdf)
                self.informacionGeneral(pdf, analisis)
                self.page_2(pdf)
                self.bases_cambio(pdf, analisis)
                self.rel_bases_cambio(pdf, analisis)
                self.extracto_salinidad(pdf, analisis)
                self.aportacion_requ(pdf, analisis)


                pdf.showPage()

                pdf.save()
                pdf = buffer.getvalue()
                buffer.close()
                response.write(pdf)
                return response

            return render(request, self.template_name, {'form': self.form, 'resultado':'sin'})



@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class Reporte_Staff_PDF(View):

    def cabecera(self,pdf):
        archivo_imagen = settings.MEDIA_ROOT+'/img/logo.png'
        pdf.drawImage(archivo_imagen, 520, 720, 56, 69, preserveAspectRatio=True)
        
    def titulo(self, pdf):
        #Estilo
        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 16)
        #pdf.setStrokeColorRGB(0.2,0.5,0.3)
        #pdf.setFillColorRGB(0,0,0.77)
        pdf.drawString(160, 750, 'Laboratorio Integral Agroalimentario')
        pdf.setFont('Helvetica', 13)
        pdf.drawString(165, 730, 'Resultados de Análisis Fisicoquimico de Suelo')

    def informacionGeneral(self, pdf, analisis):
        #estilo
        ancho_base = 30
        alto_base = 650
        inter = 25 #Interlineado
        inter_2 = 20

        ancho = ancho_base
        pdf.setFont('Helvetica-Bold', 11)
        pdf.drawString(ancho, alto_base+30 , 'INFORMACIÓN GENERAL')
        pdf.line(ancho, alto_base+28, 200, alto_base+28)
        #pdf.setFillColorRGB(1,0,1)
        

        
        #estilo
        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 10)

        alto = alto_base
        pdf.drawString(ancho, alto, 'Popietario:')
        pdf.drawString(ancho + 190, alto, 'No Registro:')
        pdf.drawString(ancho + 370, alto, 'Fecha de Recepción:')

        alto = alto-(inter*1)
        pdf.drawString(ancho, alto, 'Estado:')
        pdf.drawString(ancho + 160, alto, 'Municipio:')
        pdf.drawString(ancho + 300, alto, 'Ejido:')
        pdf.drawString(ancho + 430, alto, 'Predio:')

        alto = alto-(inter*1)
        pdf.drawString(ancho, alto, 'Cult. Anterior:')
        pdf.drawString(ancho + 130, alto, 'Cult. Sembrar:')
        pdf.drawString(ancho + 260, alto, 'Régimen Hum.:')
        pdf.drawString(ancho + 405, alto, 'Rendimiento Esperado:')
        

        #estilo
        pdf.setFont('Helvetica', 10)

        #Obtención de Valores
        Productor = valor_str_SD(analisis.productor)
        Folio = valor_str_SD(analisis.folio_str)

        if analisis.fecha_recepcion == None:
            fecha = 'S.D.'
        else:
            fecha_R = analisis.fecha_recepcion
            fecha = fecha_R.strftime("%d/%m/%Y")

        
        Estado = valor_str_SD(analisis.estado)
        Municipio = valor_str_SD(analisis.municipio)
        Localidad = valor_str_SD(analisis.localidad_ejido)
        Predio = valor_str_SD(analisis.nombre_predio)
        Cultivo_Anterior = valor_str_SD(analisis.cultivo_anterior)
        Cultivo_Establecer = valor_str_SD(analisis.cultivo_a_establecer)
        Regimen_Hidrico = valor_str_SD(analisis.regimen_hidrico)
        rendimiento = valor_str_SD(analisis.rendimiento_esperado)

        alto_d = alto_base
        pdf.drawString(ancho + 55, alto_d, Productor)
        pdf.drawString(ancho+ 253, alto_d, Folio)
        
        
        pdf.drawString(ancho + 477, alto_d, fecha)

        alto_d = alto_d-(inter*1)
        pdf.drawString(ancho + 40, alto_d, Estado[:19])
        pdf.drawString(ancho + 213, alto_d, Municipio[:15])
        pdf.drawString(ancho + 330, alto_d, Localidad[:17])
        pdf.drawString(ancho+ 465, alto_d, Predio[:12])

        alto_d = alto_d-(inter*1)
        pdf.drawString(ancho + 67, alto_d, Cultivo_Anterior)
        pdf.drawString(ancho + 200, alto_d, Cultivo_Establecer)
        pdf.drawString(ancho + 333, alto_d, Regimen_Hidrico)
        
        pdf.drawString(ancho + 517, alto_d, rendimiento)

        ###CARACTERISTICAS DEL SUELO

        ## Titulo
        alto = alto - 30
        pdf.setStrokeColorRGB(1, 1, 1)
        pdf.setFillColorRGB(0, 0.3, 0)

        pdf.rect(ancho, alto-5, 550, 20, fill=1)

        pdf.setFillColorRGB(255, 255, 255)
        pdf.setFont('Helvetica-Bold', 11)
        pdf.drawString(ancho+200, alto , 'CARACTERISTICAS DEL SUELO')
        #pdf.line(ancho, alto-2, 200, alto-2)

        pdf.setFillColorRGB(0, 0, 0)
        pdf.setStrokeColorRGB(0, 0, 0)

        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 11)

        ## Encabezados
        alto = alto -20
        pdf.drawString(ancho, alto, 'Parametro')
        pdf.drawString(ancho + 150, alto, 'Resultado')
        pdf.drawString(ancho + 350, alto, 'Interpretación')
        pdf.line(ancho, alto-3, 580, alto-3)


        ## Parametros
        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 10)

        alto = alto -20
        pdf.drawString(ancho, alto, 'ph (1:2 Agua):')
        pdf.drawString(ancho, alto - inter_2, 'CE (1:2 Agua):')
        pdf.drawString(ancho, alto - (inter_2*2), 'CIC:')
        pdf.drawString(ancho, alto - (inter_2*3), 'Densidad Aparente:')
        pdf.drawString(ancho, alto - (inter_2*4), 'Materia Orgánica:')
        pdf.drawString(ancho, alto - (inter_2*5), 'Textura:')
        pdf.drawString(ancho, alto - (inter_2*6), 'Color:')
        pdf.drawString(ancho, alto - (inter_2*7), 'Punto de Saturación:')
        pdf.drawString(ancho, alto - (inter_2*8), 'Capacidad de Campo:')
        pdf.drawString(ancho, alto - (inter_2*9), 'PMP:')
        

        ## Valores
        
        pdf.setFont('Helvetica', 10)

        ph = valor_str(analisis.ph)
        ce = valor_str(analisis.ce)
        unidad_ce = valor_str(analisis.unidad)
        cic = valor_str(analisis.Cic)
        da = valor_str(analisis.densidad_aparente)
        mo = valor_str(analisis.materia_organica)
        tex_arenas = valor_str(analisis.textura_arenas)
        tex_arcillas = valor_str(analisis.textura_arcillas)
        tex_limos = valor_str(analisis.textura_limos)
        ps = valor_str(analisis.punto_saturacion)
        cc = valor_str(analisis.capacidad_campo)
        pmp = valor_str(analisis.punto_marchitez)
        color_clave = valor_str(analisis.clave_color).title()
        color_v = valor_str(analisis.color).title()
      


        alto_d = alto_d - 70

        pdf.drawString(ancho+150 , alto_d, ph)
        pdf.drawString(ancho+150 , alto_d - inter_2, ce + ' (' + unidad_ce + ')')
        pdf.drawString(ancho+150 , alto_d - (inter_2*2), cic)
        pdf.drawString(ancho+150 , alto_d - (inter_2*3), da + '(gr/cm3)')
        pdf.drawString(ancho+150 , alto_d - (inter_2*4), mo)
        pdf.setFont('Helvetica', 9)
        pdf.drawString(ancho+150 , alto_d - (inter_2*5), 'Arenas: ' + tex_arenas + ', Arcillas: ' + tex_arenas + ', Limos: ' + tex_limos)  
        pdf.setFont('Helvetica', 10)
        pdf.drawString(ancho+150 , alto_d - (inter_2*6), color_clave + ' ' + color_v)
        pdf.drawString(ancho+150 , alto_d - (inter_2*7), ps)
        pdf.drawString(ancho+150 , alto_d - (inter_2*8), cc)
        pdf.drawString(ancho+150 , alto_d - (inter_2*9), pmp)

        ## Interpretación
        pdf.drawString(ancho+350 , alto_d, valor_str(analisis.clasificacion_ph))
        pdf.drawString(ancho+350 , alto_d - inter_2, valor_str(analisis.clasificacion_ce).title())
        pdf.drawString(ancho+350 , alto_d - (inter_2*4), valor_str(analisis.interpretacionMO))
        pdf.drawString(ancho+350 , alto_d - (inter_2*5), valor_str(analisis.textura_textura).title())


        ### NUTRIENTES Y FERTILIDAD
        alto = alto - (inter_2*9) - 30
        pdf.setStrokeColorRGB(1, 1, 1)
        pdf.setFillColorRGB(0, 0.3, 0)

        pdf.rect(ancho, alto-5, 550, 20, fill=1)

        pdf.setFillColorRGB(255, 255, 255)
        pdf.setFont('Helvetica-Bold', 11)
        pdf.drawString(ancho+200, alto , 'NUTRIENTES Y FERTILIDAD DEL SUELO')
        #pdf.line(ancho, alto-2, 200, alto-2)

        pdf.setFillColorRGB(0, 0, 0)
        pdf.setStrokeColorRGB(0, 0, 0)

        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 7)

        ## Encabezados
        alto = alto -20
        pdf.drawString(ancho+7, alto, 'Determinación')
        pdf.drawString(ancho + 70, alto, 'Unidades')
        pdf.drawString(ancho + 125, alto, 'Resultado')

        # Rectangulos Encabezados Verticales
        pdf.rect(ancho, alto+15, 60, -230)
        pdf.rect(ancho+60, alto+15, 55, -230)
        pdf.rect(ancho+60+55, alto+15, 57, -230)

        # Rectagungulo para delimitar area
        pdf.rect(ancho+172,alto-5, 7*54, -210)

        # Rectangulo Encabezados Horizontal
        pdf.rect(ancho, alto-5, 60+55+57, 20)

        # Rectangulos de divisiones de Encabezados Escalas
        pdf.rect(ancho+172, alto-5, 378, 20)
        pdf.rect(ancho+172, alto-5, 54, 20)
        pdf.rect(ancho+226, alto-5, 54, 20)
        pdf.rect(ancho+280, alto-5, 54, 20)
        pdf.rect(ancho+334, alto-5, 54, 20)
        pdf.rect(ancho+388, alto-5, 54, 20)
        pdf.rect(ancho+442, alto-5, 54, 20)
        pdf.rect(ancho+496, alto-5, 54, 20)

        pdf.setFont('Helvetica', 7)

        # Encabezados de Escalas
        pdf.drawString(ancho+184, alto, 'Muy Bajo')
        pdf.drawString(ancho+226+15, alto, 'Bajo')
        pdf.drawString(ancho+280+15, alto, 'Mod. Bajo')
        pdf.drawString(ancho+334+15, alto, 'Mediano')
        pdf.drawString(ancho+388+15, alto, 'Mod. Alto')
        pdf.drawString(ancho+442+15, alto, 'Alto')
        pdf.drawString(ancho+496+15, alto, 'Muy Alto')


        # Nombre del Elemento
        pdf.setFont('Helvetica', 9)
        pdf.drawString(ancho+7, alto-inter_2, 'N-Inorg')
        pdf.drawString(ancho+7, alto-(inter_2*2), valor_str(analisis.tipo_fosforo))
        pdf.drawString(ancho+7, alto-(inter_2*3), 'K')
        pdf.drawString(ancho+7, alto-(inter_2*4), 'Ca')
        pdf.drawString(ancho+7, alto-(inter_2*5), 'Mg')
        pdf.drawString(ancho+7, alto-(inter_2*6), 'Na')
        pdf.drawString(ancho+7, alto-(inter_2*7), 'Fe')
        pdf.drawString(ancho+7, alto-(inter_2*8), 'Zn')
        pdf.drawString(ancho+7, alto-(inter_2*9), 'Mn')
        pdf.drawString(ancho+7, alto-(inter_2*10), 'Cu')
        #pdf.drawString(ancho+7, alto-(inter_2*11), 'B')
        #pdf.drawString(ancho+7, alto-(inter_2*12), 'P-Olsen')

        # Unidades
        pdf.drawString(ancho+73, alto-inter_2, '(ppm)')
        pdf.drawString(ancho+73, alto-(inter_2*2), '(ppm)')
        pdf.drawString(ancho+73, alto-(inter_2*3), '(ppm)')
        pdf.drawString(ancho+73, alto-(inter_2*4), '(ppm)')
        pdf.drawString(ancho+73, alto-(inter_2*5), '(ppm)')
        pdf.drawString(ancho+73, alto-(inter_2*6), '(ppm)')
        pdf.drawString(ancho+73, alto-(inter_2*7), '(ppm)')
        pdf.drawString(ancho+73, alto-(inter_2*8), '(ppm)')
        pdf.drawString(ancho+73, alto-(inter_2*9), '(ppm)')
        pdf.drawString(ancho+73, alto-(inter_2*10), '(ppm)')
        #pdf.drawString(ancho+73, alto-(inter_2*11), '(ppm)')
        #pdf.drawString(ancho+73, alto-(inter_2*12), '(ppm)')


        # Resultados de Nutrientes
        N = analisis.nitrogeno
        P = analisis.fosforo
        K = analisis.K
        Ca = analisis.Ca
        Mg = analisis.Mg
        Na = analisis.Na
        Fe = analisis.Fe
        Zn = analisis.Zn
        Mn = analisis.Mn
        Cu = analisis.Cu


        pdf.drawString(ancho+128, alto-inter_2, str(N))
        pdf.drawString(ancho+128, alto-(inter_2*2), str(P))
        pdf.drawString(ancho+128, alto-(inter_2*3), str(K))
        pdf.drawString(ancho+128, alto-(inter_2*4), str(Ca))
        pdf.drawString(ancho+128, alto-(inter_2*5), str(Mg))
        pdf.drawString(ancho+128, alto-(inter_2*6), str(Na))
        pdf.drawString(ancho+128, alto-(inter_2*7), str(Fe))
        pdf.drawString(ancho+128, alto-(inter_2*8), str(Zn))
        pdf.drawString(ancho+128, alto-(inter_2*9), str(Mn))
        pdf.drawString(ancho+128, alto-(inter_2*10), str(Cu))
        #pdf.drawString(ancho+128, alto-(inter_2*11), 'N.D')

        # **************************************************************
        # Datos para Graficas Elementos
        N_clas = clas_N(analisis.nitrogeno)
        P_clas = clas_P(analisis.fosforo, analisis.tipo_fosforo)
        K_clas = clas_K(analisis.K)
        Ca_clas = clas_Ca(analisis.Ca)
        Mg_clas = clas_Mg(analisis.Mg)
        Na_clas = clas_Na(analisis.Na)
        Fe_clas = clas_Fe(analisis.Fe)
        Zn_clas = clas_Zn(analisis.Zn)
        Mn_clas = clas_Mn(analisis.Mn)
        Cu_clas = clas_Cu(analisis.Cu)

        # Color del borde de las barras(graficas)
        pdf.setStrokeColorRGB(1, 1, 1)

        # Nitrogeno
        pdf.setFillColorRGB(.3765,.7882,.2196)
        pdf.rect(ancho+172, alto-inter_2+8, N_clas['valor'], -10, fill=1)
       
       # Fosforo
        pdf.setFillColorRGB(.302,.5882,.0353)
        pdf.rect(ancho+172, alto-(inter_2*2)+8, P_clas['valor'], -10, fill=1)

        # Potasio
        pdf.setFillColorRGB(.9294,.1961,.2118)
        pdf.rect(ancho+172, alto-(inter_2*3)+8, K_clas['valor'], -10, fill=1)

        #Calcio
        pdf.setFillColorRGB(.949,.6627,.3529)
        pdf.rect(ancho+172, alto-(inter_2*4)+8, Ca_clas['valor'], -10, fill=1)

        # Magnesio
        pdf.setFillColorRGB(.749,.4235,.0745)
        pdf.rect(ancho+172, alto-(inter_2*5)+8,  Mg_clas['valor'], -10, fill=1)

        # Sodio
        pdf.setFillColorRGB(.9804,.0275,.6471)
        pdf.rect(ancho+172, alto-(inter_2*6)+8, Na_clas['valor'], -10, fill=1)

        # Hierro
        pdf.setFillColorRGB(.7098,.8392,.80)
        pdf.rect(ancho+172, alto-(inter_2*7)+8, Fe_clas['valor'], -10, fill=1)

        # Zinc
        pdf.setFillColorRGB(.1725,.5216,.5216)
        pdf.rect(ancho+172, alto-(inter_2*8)+8, Zn_clas['valor'], -10, fill=1)

        # Manganeso
        pdf.setFillColorRGB(.0667,.1686,.8392)
        pdf.rect(ancho+172, alto-(inter_2*9)+8, Mn_clas['valor'], -10, fill=1)

        #Cobre
        pdf.setFillColorRGB(.0078,.6824,.749)
        pdf.rect(ancho+172, alto-(inter_2*10)+8, Cu_clas['valor'], -10, fill=1)

    def page_2(self, pdf):
        pdf.showPage()

        archivo_imagen = settings.MEDIA_ROOT+'/img/logo.png'
        pdf.drawImage(archivo_imagen, 520, 720, 56, 69, preserveAspectRatio=True)

        #Estilo
        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 16)
        #pdf.setStrokeColorRGB(0.2,0.5,0.3)
        #pdf.setFillColorRGB(0,0,0.77)
        pdf.drawString(160, 750, 'Laboratorio Integral Agroalimentario')
        pdf.setFont('Helvetica', 13)
        pdf.drawString(165, 730, 'Resultados de Análisis Fisicoquimico de Suelo')

    def bases_cambio(self, pdf, analisis):
        ancho_base = 30
        alto_base = 650
        inter = 25 #Interlineado
        inter_2 = 20

        ## Subtitulo
        alto = alto_base + 50
        ancho = ancho_base
        pdf.setStrokeColorRGB(1, 1, 1)
        pdf.setFillColorRGB(0, 0.3, 0)

        pdf.rect(ancho, alto-5, 550, 20, fill=1)

        pdf.setFillColorRGB(255, 255, 255)
        pdf.setFont('Helvetica-Bold', 11)
        pdf.drawString(ancho+100, alto , 'PORCENTAJE ACTUAL Y SUGERIDO DE LAS BASES DE CAMBIO')
        
        ### TABLA
        pdf.setFillColorRGB(0, 0, 0)
        pdf.setStrokeColorRGB(0, 0, 0)

        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 9)

        ## Encabezados
        alto = alto -20
        adicion_ancho = 55
        pdf.drawString(ancho+7, alto, 'Determinación')
        pdf.drawString(ancho + 90, alto, 'Unidades')
        pdf.drawString(ancho + 170, alto, 'H+')
        pdf.drawString(ancho + 170 + (adicion_ancho * 1), alto, 'Al++')
        pdf.drawString(ancho + 170 + (adicion_ancho * 2), alto, 'Ca++')
        pdf.drawString(ancho + 170 + (adicion_ancho * 3), alto, 'Mg++')
        pdf.drawString(ancho + 170 + (adicion_ancho * 4), alto, 'K++')
        pdf.drawString(ancho + 170 + (adicion_ancho * 5), alto, 'Na++')
        pdf.drawString(ancho + 170 + (adicion_ancho * 6), alto, 'CIC+')

        
        pdf.setFont('Helvetica', 9)

        alto = alto
        alto_rec = alto + 5
        
        # Determinación y Unidades
        pdf.drawString(ancho + 7, alto - (inter*2) / 1.25, 'Resultado')
        pdf.drawString(ancho + 90, alto - inter, 'meq/100gr')
        pdf.drawString(ancho + 90, alto - inter * 2, '% Actual')
        pdf.drawString(ancho + 7, alto - inter * 3, 'Sugerido')
        pdf.drawString(ancho + 90, alto - inter * 3, '% Sugerido')

        # Sugerido (Valores)
        pdf.drawString(ancho + 165, alto - inter * 3, '0 - 5')
        pdf.drawString(ancho + 165 + (adicion_ancho * 1), alto - inter * 3, '0 - 0.1')
        pdf.drawString(ancho + 165 + (adicion_ancho * 2), alto - inter * 3, '65 - 75')
        pdf.drawString(ancho + 165 + (adicion_ancho * 3), alto - inter * 3, '10 - 20')
        pdf.drawString(ancho + 165 + (adicion_ancho * 4), alto - inter * 3, '3 - 7')
        pdf.drawString(ancho + 165 + (adicion_ancho * 5), alto - inter * 3, '0 - 5')

        # Rectangulos para formar la tabla (Verticales)
        pdf.rect(ancho, alto_rec + 10, 75, -100)
        pdf.rect(ancho + 75, alto_rec+10, 75, -100)
        pdf.rect(ancho + 150, alto_rec+10, adicion_ancho, -100)
        pdf.rect(ancho + 150 + (adicion_ancho*1), alto_rec+10, adicion_ancho, -100)
        pdf.rect(ancho + 150 + (adicion_ancho*2), alto_rec+10, adicion_ancho, -100)
        pdf.rect(ancho + 150 + (adicion_ancho*3), alto_rec+10, adicion_ancho, -100)
        pdf.rect(ancho + 150 + (adicion_ancho*4), alto_rec+10, adicion_ancho, -100)
        pdf.rect(ancho + 150 + (adicion_ancho*5), alto_rec+10, adicion_ancho, -100)
        pdf.rect(ancho + 150 + (adicion_ancho*6), alto_rec+10, 70, -100)

        # Rectangulos para formar la tabla (Horizontales)
        pdf.rect(ancho, alto_rec + 10 - inter, 75, - (inter * 2)) # Resultado

        pdf.rect(ancho, alto_rec+10, 550, -inter)
        pdf.rect(ancho + 75, alto_rec+10-(inter*1),75 + (adicion_ancho*6), -inter)
        pdf.rect(ancho + 75, alto_rec+10-(inter*2),75 + (adicion_ancho*6), -inter)
        pdf.rect(ancho + 75, alto_rec+10-(inter*3),75 + (adicion_ancho*6), -inter)

        ## OBTENCIÓN DE VALORES
        CaMeq = valor_str(analisis.CaMeq)
        MgMeq = valor_str(analisis.MgMeq)
        NaMeq = valor_str(analisis.NaMeq)
        KMeq = valor_str(analisis.KMeq)
        Cic = valor_str(analisis.Cic)
        CaPorcentaje = valor_str(analisis.CaPorcentaje)
        MgPorcentaje = valor_str(analisis.MgPorcentaje)
        NaPorcentaje = valor_str(analisis.NaPorcentaje)
        KPorcentaje = valor_str(analisis.KPorcentaje)

        # Impresión de Valores
        # H+
        pdf.drawString(ancho + 165, alto - (inter * 1), 'N.D.')
        pdf.drawString(ancho + 165, alto - (inter * 2), 'N.D.')
        # Al++
        pdf.drawString(ancho + 165 + (adicion_ancho * 1), alto - (inter * 1), 'N.D.')
        pdf.drawString(ancho + 165 + (adicion_ancho * 1), alto - (inter * 2), 'N.D.')
        # Ca++
        pdf.drawString(ancho + 165 + (adicion_ancho * 2), alto - (inter * 1), CaMeq)
        pdf.drawString(ancho + 165 + (adicion_ancho * 2), alto - (inter * 2), CaPorcentaje)
        # Mg++
        pdf.drawString(ancho + 165 + (adicion_ancho * 3), alto - (inter * 1), MgMeq)
        pdf.drawString(ancho + 165 + (adicion_ancho * 3), alto - (inter * 2), MgPorcentaje)
        # Mg++
        pdf.drawString(ancho + 165 + (adicion_ancho * 4), alto - (inter * 1), KMeq)
        pdf.drawString(ancho + 165 + (adicion_ancho * 4), alto - (inter * 2), KPorcentaje)
        # Na++
        pdf.drawString(ancho + 165 + (adicion_ancho * 5), alto - (inter * 1), NaMeq)
        pdf.drawString(ancho + 165 + (adicion_ancho * 5), alto - (inter * 2), NaPorcentaje)
        # CIC
        pdf.drawString(ancho + 165 + (adicion_ancho * 6), alto - (inter * 2), Cic)

    def rel_bases_cambio(self, pdf, analisis):
        ancho = 30
        alto = 650 - (25*4)
        inter = 25 #Interlineado
        inter_grafi = 30
        inter_2 = 20
       
       ## Subtitulo 1
        pdf.setStrokeColorRGB(1, 1, 1)
        pdf.setFillColorRGB(0, 0.3, 0)

        pdf.rect(ancho, alto-5, 250, 20, fill=1)

        pdf.setFillColorRGB(255, 255, 255)
        pdf.setFont('Helvetica-Bold', 11)
        pdf.drawString(ancho+40, alto , 'RELACIÓN DE BASES DE CAMBIO')

         ## Subtitulo 2
        pdf.setStrokeColorRGB(1, 1, 1)
        pdf.setFillColorRGB(0, 0.3, 0)

        pdf.rect(ancho + 260 , alto-5, 290, 20, fill=1)

        pdf.setFillColorRGB(255, 255, 255)
        pdf.setFont('Helvetica-Bold', 11)
        pdf.drawString(ancho+305, alto , 'EXTRACTO DE SALINIDAD Y SODICIDAD')

        ## Grafico
        pdf.setFillColorRGB(0, 0, 0)
        pdf.setStrokeColorRGB(0, 0, 0)

        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 9)

        alto = alto - inter_grafi
        ancho_txt = ancho + 10
        pdf.drawString(ancho_txt, alto, 'Muy Alto')
        pdf.drawString(ancho_txt, alto- (inter_grafi * 1), 'Alto')
        pdf.drawString(ancho_txt, alto- (inter_grafi * 2), 'Mediano')
        pdf.drawString(ancho_txt, alto- (inter_grafi * 3), 'Bajo')
        pdf.drawString(ancho_txt, alto- (inter_grafi * 4), 'Muy Bajo')

        ## Rectangulo grafico
        y_rec = alto + 17
        largo_rec = 65
        ancho_rec = 30
        pdf.rect(ancho, y_rec, largo_rec, -ancho_rec)
        pdf.rect(ancho, y_rec - (ancho_rec * 1), largo_rec, -ancho_rec)
        pdf.rect(ancho, y_rec - (ancho_rec * 2), largo_rec, -ancho_rec)
        pdf.rect(ancho, y_rec - (ancho_rec * 3), largo_rec, -ancho_rec)
        pdf.rect(ancho, y_rec - (ancho_rec * 4), largo_rec, -ancho_rec)

        ## TABLA INFERIOR DEL GRAFICO
        #Texto
        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 8)

        alto_txt_tabla = alto -(inter_grafi * 5)
        ancho_txt_tabla = ancho + 10
        y_txt_vertical = alto_txt_tabla + 5
        #Encabezados Verticales
        pdf.drawString(ancho_txt_tabla, y_txt_vertical, 'Relación')
        pdf.drawString(ancho_txt_tabla, y_txt_vertical - (inter_2 * 1), 'Resultado')
        pdf.drawString(ancho_txt_tabla, y_txt_vertical - (inter_2 * 2), 'Rango Medio')

        # Encabezados Horizontales
        pdf.setFont('Helvetica-Bold', 7)
        ancho_in_enc_ho = ancho + largo_rec + 15
        ancho_text_ho = 45
        pdf.drawString(ancho_in_enc_ho, y_txt_vertical, 'Ca/Mg')
        pdf.drawString(ancho_in_enc_ho + (ancho_text_ho * 1), y_txt_vertical, 'Mg/K')
        pdf.drawString(ancho_in_enc_ho-5 + (ancho_text_ho * 2), y_txt_vertical, 'Ca+Mg/K')
        pdf.drawString(ancho_in_enc_ho + (ancho_text_ho * 3), y_txt_vertical, 'Ca/K')

        # Rectangulos Verticales
        y_rec = alto_txt_tabla + 17
        largo_rec = ancho_text_ho
        ancho_rec = (inter_2 * 3)
        pdf.rect(ancho, y_rec, 65, -ancho_rec)
        # pdf.rect(ancho + 75, y_rec, largo_rec, -ancho_rec)
        # pdf.rect(ancho + 75 + (largo_rec * 1), y_rec, largo_rec, -ancho_rec)
        # pdf.rect(ancho + 75 + (largo_rec * 2), y_rec, largo_rec, -ancho_rec)
        # pdf.rect(ancho + 75 + (largo_rec * 3), y_rec, largo_rec, -ancho_rec)

        # Rectangulo Horizontal Unico
        pdf.rect(ancho, y_rec - (inter_2 * 0), 60 + (largo_rec * 4), -20)
        pdf.rect(ancho, y_rec - (inter_2 * 1), 60 + (largo_rec * 4), -20)

        # Rectangulo que enmarca la grafica
        pdf.rect(ancho, alto+17, 240, -150-(inter_2*3))

        # Obtención de valores y resultados
        Ca_Mg = valor_str(analisis.Ca_Mg)
        Mg_K = valor_str(analisis.Mg_K)
        CaMg_K = valor_str(analisis.CaMg_K)
        Ca_K = valor_str(analisis.Ca_K)

        # Impresión de valores en la tabla
        x_val = ancho + 80
        y_val = y_txt_vertical - inter_2
        x_aum = ancho_text_ho

        pdf.drawString(x_val, y_val, Ca_Mg)
        pdf.drawString(x_val + (x_aum * 1), y_val, Mg_K)
        pdf.drawString(x_val + (x_aum * 2), y_val, CaMg_K)
        pdf.drawString(x_val + (x_aum * 3), y_val, Ca_K)

        # Impresión de Rango Medio
        pdf.drawString(x_val, y_val - inter_2, "2 - 6")
        pdf.drawString(x_val + (x_aum * 1), y_val - inter_2, "2 - 3")
        pdf.drawString(x_val + (x_aum * 2), y_val - inter_2, "20 - 30")
        pdf.drawString(x_val + (x_aum * 3), y_val - inter_2, "10 - 15")

        # Gaficar Resultados

            ## Obtención de resultados clasificación
        Ca_Mg_class = clas_Ca_Mg(analisis.Ca_Mg)
        Mg_K_class = clas_Ca_Mg(analisis.Mg_K)
        CaMg_K_class = clas_Ca_Mg(analisis.CaMg_K)
        Ca_K_class = clas_Ca_Mg(analisis.Ca_K)

        pdf.setStrokeColorRGB(1, 1, 1)
        pdf.setFillColorRGB(.0039,.7020,.9922)

        #Rectangulo (inicio en x, inicio en Y, Largo, Ancho)
        base_x = x_val+3
        base_y = y_txt_vertical + 12
        largo_graf = 12
        aumento_x = 45
        escala_base = 30
        pdf.rect(base_x, base_y, largo_graf, Ca_Mg_class['valor'], fill=1)
        pdf.rect(base_x + (aumento_x * 1), base_y, largo_graf, Mg_K_class['valor'], fill=1)
        pdf.rect(base_x + (aumento_x * 2), base_y, largo_graf, CaMg_K_class['valor'], fill=1)
        pdf.rect(base_x + (aumento_x * 3), base_y, largo_graf, Ca_K_class['valor'], fill=1)
        

    def extracto_salinidad(self, pdf, analisis):
        base_x = 290
        base_y = 520
        inter = 20

        ## OBTENCIÓN DE RESULTADOS
        ph_pasta = valor_str(analisis.ph_pasta)
        ce_pasta = valor_str(analisis.ce_pasta)
        unidad_cePasta = valor_str(analisis.unidad_cePasta)
        Ras = valor_str(analisis.Ras)
        Psi = valor_str(analisis.Psi)
        CaCation = valor_str(analisis.CaCation)
        MgCation = valor_str(analisis.MgCation)
        NaCation = valor_str(analisis.NaCation)
        KCation = valor_str(analisis.KCation)
        carbonatos = valor_str(analisis.carbonatos)
        bicarbonatos = valor_str(analisis.bicarbonatos)
        cloruros = valor_str(analisis.cloruros)
        sulfatos = valor_str(analisis.sulfatos)



        pdf.setFillColorRGB(0, 0, 0)
        pdf.setStrokeColorRGB(0, 0, 0)

        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 8)

        # Concepto Parte Superior
        txt_x = base_x + 10
        txt_y = base_y
        incre_x = 90
        pdf.drawString(txt_x, txt_y, "Cee")
        pdf.drawString(txt_x, txt_y - inter, "pHe")
        pdf.drawString(txt_x + incre_x, txt_y, "RAS")
        pdf.drawString(txt_x + incre_x, txt_y - inter, "PSI")

        #Resultados Parte Superior
        txt_x2 = txt_x + 25
        pdf.setFont('Helvetica', 8)
        pdf.drawString(txt_x2, txt_y, ce_pasta + "( "+ unidad_cePasta +")")
        pdf.drawString(txt_x2, txt_y - inter, ph_pasta)
        pdf.drawString(txt_x2 + incre_x, txt_y, Ras)
        pdf.drawString(txt_x2 + incre_x, txt_y - inter, Psi)


        #Encabezado Segundo cuadro
        pdf.setFont('Helvetica-Bold', 10)
        txt_y2 = txt_y - (inter * 3)
        txt_x_b = base_x + 5
        pdf.drawString(txt_x_b, txt_y2, "Cationes (Meq/l)")
        pdf.drawString(txt_x_b + incre_x, txt_y2, "Aniones (Meq/l)")

        # Conceptos Parte Inferior
        pdf.setFont('Helvetica-Bold', 8)
        txt_y3 = txt_y2 - inter 
            # Cationes  
        pdf.drawString(txt_x, txt_y3, "Ca++")
        pdf.drawString(txt_x, txt_y3 - (inter * 1), "Mg++")
        pdf.drawString(txt_x, txt_y3 - (inter * 2), "Na+")
        pdf.drawString(txt_x, txt_y3 - (inter * 3), "K+")
        pdf.drawString(txt_x, txt_y3 - (inter * 4), "PO4")

            # Aniones  
        pdf.drawString(txt_x + incre_x, txt_y3, "CO3")
        pdf.drawString(txt_x + incre_x, txt_y3 - (inter * 1), "HCO3")
        pdf.drawString(txt_x + incre_x, txt_y3 - (inter * 2), "Cl-")
        pdf.drawString(txt_x + incre_x, txt_y3 - (inter * 3), "SO4")
        pdf.drawString(txt_x + incre_x, txt_y3 - (inter * 4), "N-NO3")

       #Resultados Parte Inferior
        txt_x3 = txt_x + 30
        pdf.setFont('Helvetica', 8)
            # Cationes  
        pdf.drawString(txt_x3, txt_y3, CaCation)
        pdf.drawString(txt_x3, txt_y3 - (inter * 1), MgCation)
        pdf.drawString(txt_x3, txt_y3 - (inter * 2), NaCation)
        pdf.drawString(txt_x3, txt_y3 - (inter * 3), KCation)
        pdf.drawString(txt_x3, txt_y3 - (inter * 4), "N.D.")
        
            # Aniones  
        pdf.drawString(txt_x3 + incre_x, txt_y3, carbonatos)
        pdf.drawString(txt_x3 + incre_x, txt_y3 - (inter * 1), bicarbonatos)
        pdf.drawString(txt_x3 + incre_x, txt_y3 - (inter * 2), cloruros)
        pdf.drawString(txt_x3 + incre_x, txt_y3 - (inter * 3), sulfatos)
        pdf.drawString(txt_x3 + incre_x, txt_y3 - (inter * 4), "N.D.")

        ## Rectangulo Tabla
        rec_tabla_y = base_y + 17
        rec_tabla_x = base_x
        pdf.rect(rec_tabla_x, rec_tabla_y, 172, -190)


        ###GRAFICO
        graf_x = txt_x3 + 140
        graf_y = base_y
        graf_inter = 30

        pdf.setFont('Helvetica-Bold', 8)
        pdf.drawString(graf_x, graf_y, 'Muy Alto')
        pdf.drawString(graf_x, graf_y - (graf_inter * 1), 'Alto')
        pdf.drawString(graf_x, graf_y - (graf_inter * 2), 'Mod. Alto')
        pdf.drawString(graf_x, graf_y - (graf_inter * 3), 'Mediano')
        pdf.drawString(graf_x, graf_y - (graf_inter * 4), 'Mod. Bajo')
        pdf.drawString(graf_x, graf_y - (graf_inter * 5), 'Bajo')
        pdf.drawString(graf_x, graf_y - (graf_inter * 6), 'Muy Bajo')

        ## Rectangulo Grafico
        rec_graf_y = graf_y + 17
        rec_graf_x = graf_x - 5
        pdf.rect(rec_graf_x, rec_graf_y, 115, -210)

        ## Rectangulos Escalas de Valores
        alto_rec = graf_inter
        largo_rec = 45
        
        pdf.rect(rec_graf_x, rec_graf_y, largo_rec, -alto_rec)
        pdf.rect(rec_graf_x, rec_graf_y - (alto_rec * 1), largo_rec, -alto_rec)
        pdf.rect(rec_graf_x, rec_graf_y - (alto_rec * 2), largo_rec, -alto_rec)
        pdf.rect(rec_graf_x, rec_graf_y - (alto_rec * 3), largo_rec, -alto_rec)
        pdf.rect(rec_graf_x, rec_graf_y - (alto_rec * 4), largo_rec, -alto_rec)
        pdf.rect(rec_graf_x, rec_graf_y - (alto_rec * 5), largo_rec, -alto_rec)
        pdf.rect(rec_graf_x, rec_graf_y - (alto_rec * 6), largo_rec, -alto_rec)

        # Texto Base de Grafica
        txt_base_graf_x = graf_x
        txt_base_graf_y = graf_y - 205
        incre_x_b = 47

        pdf.drawString(txt_base_graf_x, txt_base_graf_y, 'Grado de')
        pdf.setFont('Helvetica', 8)
        pdf.drawString(txt_base_graf_x + (incre_x_b * 1), txt_base_graf_y, 'Sales')
        pdf.drawString(txt_base_graf_x + (incre_x_b * 2)-7, txt_base_graf_y, 'RAS')

        # Gaficar Resultados
        pdf.setStrokeColorRGB(1, 1, 1)
        pdf.setFillColorRGB(.0039,.7020,.9922)

                    #Rectangulo (inicio en x, inicio en Y, Largo, Ancho)

        ## Valores para grafico 
        sales_clas = clas_Sales(analisis.NaCation)
        rass_clas = clas_RAS(analisis.Ras)

        base_x = txt_base_graf_x + 50
        base_y = txt_base_graf_y + 12
        largo_graf = 12
        aumento_x = 40
        escala_base = alto_rec
        pdf.rect(base_x, base_y, largo_graf, sales_clas['valor'], fill=1)
        pdf.rect(base_x + (aumento_x * 1), base_y, largo_graf, rass_clas['valor'], fill=1)
        

    def aportacion_requ(self, pdf, analisis):
        base_x = 30
        base_y = 280
        inter = 20
        

        ## Encabezado Principal
        pdf.setStrokeColorRGB(1, 1, 1)
        pdf.setFillColorRGB(0, 0.3, 0)

        pdf.rect(base_x, base_y, 550, 20, fill=1)

        pdf.setFillColorRGB(255, 255, 255)
        pdf.setFont('Helvetica-Bold', 14)
        pdf.drawString(base_x+70, base_y+5 , 'Requerimientos, Aportación y Necesidades de Nutrientes')

        #Subtitulos
        pdf.setFillColorRGB(0, 0, 0)
        pdf.setStrokeColorRGB(0, 0, 0)

        pdf.setLineWidth(.3)
        pdf.setFont('Helvetica-Bold', 10)

        subtitulo_x = base_x + 120
        pdf.drawString(subtitulo_x, base_y - inter, "Necesidades de Nutrientes para el Rendimiento Esperado (kg/ha)")
        pdf.drawString(subtitulo_x + 50, base_y - inter * 5, "Nutrientes Existentes en el Suelo  (kg/ha)")
        pdf.drawString(subtitulo_x + 50, base_y - inter * 8, "Aportación Requerida (kg/ha)")

        #Subtitulos Elementos
        elemento_x = base_x + 10
        incremento_x = 40
        pdf.drawString(elemento_x, base_y - (inter * 2), "N")
        pdf.drawString(elemento_x +(incremento_x * 1), base_y - (inter * 2), "P")
        pdf.drawString(elemento_x +(incremento_x * 2), base_y - (inter * 2), "K")
        pdf.drawString(elemento_x +(incremento_x * 3), base_y - (inter * 2), "Ca")
        pdf.drawString(elemento_x +(incremento_x * 4), base_y - (inter * 2), "Mg")
        pdf.drawString(elemento_x +(incremento_x * 5), base_y - (inter * 2), "S")
        pdf.drawString(elemento_x +(incremento_x * 6), base_y - (inter * 2), "B")
        pdf.drawString(elemento_x +(incremento_x * 7), base_y - (inter * 2), "Cl")
        pdf.drawString(elemento_x +(incremento_x * 8), base_y - (inter * 2), "Cu")
        pdf.drawString(elemento_x +(incremento_x * 9), base_y - (inter * 2), "Fe")
        pdf.drawString(elemento_x +(incremento_x * 10), base_y - (inter * 2), "Mn")
        pdf.drawString(elemento_x +(incremento_x * 11), base_y - (inter * 2), "Mo")
        pdf.drawString(elemento_x +(incremento_x * 12), base_y - (inter * 2), "Zn")
        pdf.drawString(elemento_x +(incremento_x * 13), base_y - (inter * 2), "Ni")

        # Valores Necesidades
        necesidades = requerimiento_Nutrientes(analisis.cultivo_a_establecer, analisis.rendimiento_esperado)
        
        # Valores Kg Existentes
        N_e = ppm_kg_ha(analisis.nitrogeno, 30, analisis.densidad_aparente) 
        P_e = ppm_kg_ha(analisis.fosforo, 30, analisis.densidad_aparente) 
        K_e = ppm_kg_ha(analisis.K, 30, analisis.densidad_aparente) 
        Ca_e = ppm_kg_ha(analisis.Ca, 30, analisis.densidad_aparente) 
        Mg_e = ppm_kg_ha(analisis.Mg, 30, analisis.densidad_aparente) 
        S_e = "N.D." 
        B_e = "N.D." 
        Cl_e = "N.D." 
        Cu_e = ppm_kg_ha(analisis.Cu, 30, analisis.densidad_aparente) 
        Fe_e = ppm_kg_ha(analisis.Fe, 30, analisis.densidad_aparente) 
        Mn_e = ppm_kg_ha(analisis.Mn, 30, analisis.densidad_aparente) 
        Mo_e = "N.D." 
        Zn_e = ppm_kg_ha(analisis.Zn, 30, analisis.densidad_aparente) 
        Ni_e = "N.D."

        # Valores Aportación Requerida
        N_a = aportacion_requerida(analisis.nitrogeno, 'N', analisis.cultivo_a_establecer, analisis.rendimiento_esperado, 30, analisis.densidad_aparente)
        P_a = aportacion_requerida(analisis.fosforo, 'P', analisis.cultivo_a_establecer, analisis.rendimiento_esperado, 30, analisis.densidad_aparente)
        K_a = aportacion_requerida(analisis.K, 'K', analisis.cultivo_a_establecer, analisis.rendimiento_esperado, 30, analisis.densidad_aparente)
        Ca_a = aportacion_requerida(analisis.Ca, 'Ca', analisis.cultivo_a_establecer, analisis.rendimiento_esperado, 30, analisis.densidad_aparente)
        Mg_a = aportacion_requerida(analisis.Mg, 'Mg', analisis.cultivo_a_establecer, analisis.rendimiento_esperado, 30, analisis.densidad_aparente)
        S_a = "N.D."
        B_a = "N.D."
        Cl_a = "N.D."
        Cu_a = aportacion_requerida(analisis.Cu, 'Cu', analisis.cultivo_a_establecer, analisis.rendimiento_esperado, 30, analisis.densidad_aparente)
        Fe_a = aportacion_requerida(analisis.Fe, 'Fe', analisis.cultivo_a_establecer, analisis.rendimiento_esperado, 30, analisis.densidad_aparente)
        Mn_a = aportacion_requerida(analisis.Mn, 'Mn', analisis.cultivo_a_establecer, analisis.rendimiento_esperado, 30, analisis.densidad_aparente)
        Mo_a = "N.D."
        Zn_a = aportacion_requerida(analisis.Zn, 'Zn', analisis.cultivo_a_establecer, analisis.rendimiento_esperado, 30, analisis.densidad_aparente)
        Ni_a = "N.D."

        # Impresión de valores necesidades
        pdf.setFont('Helvetica', 8)
        res_x = base_x + 5
        res_y = base_y - (inter * 3)
        pdf.drawString(res_x, res_y, str(necesidades['N']))
        pdf.drawString(res_x + (incremento_x * 1), res_y, str(necesidades['P']))
        pdf.drawString(res_x + (incremento_x * 2), res_y, str(necesidades['K']))
        pdf.drawString(res_x + (incremento_x * 3), res_y, str(necesidades['Ca']))
        pdf.drawString(res_x + (incremento_x * 4), res_y, str(necesidades['Mg']))
        pdf.drawString(res_x + (incremento_x * 5), res_y, str(necesidades['S']))
        pdf.drawString(res_x + (incremento_x * 6), res_y, str(necesidades['B']))
        pdf.drawString(res_x + (incremento_x * 7), res_y, str(necesidades['Cl']))
        pdf.drawString(res_x + (incremento_x * 8), res_y, str(necesidades['Cu']))
        pdf.drawString(res_x + (incremento_x * 9), res_y, str(necesidades['Fe']))
        pdf.drawString(res_x + (incremento_x * 10), res_y, str(necesidades['Mn']))
        pdf.drawString(res_x + (incremento_x * 11), res_y, str(necesidades['Mo']))
        pdf.drawString(res_x + (incremento_x * 12), res_y, str(necesidades['Zn']))
        pdf.drawString(res_x + (incremento_x * 13), res_y, str(necesidades['Ni']))

        # Impresión de valores Kg/Ha Existentes
        
        res_y2 = base_y - (inter * 6)
        pdf.drawString(res_x, res_y2, str(N_e))
        pdf.drawString(res_x + (incremento_x * 1), res_y2, str(P_e))
        pdf.drawString(res_x + (incremento_x * 2), res_y2, str(K_e))
        pdf.drawString(res_x + (incremento_x * 3), res_y2, str(Ca_e))
        pdf.drawString(res_x + (incremento_x * 4), res_y2, str(Mg_e))
        pdf.drawString(res_x + (incremento_x * 5), res_y2, str(S_e))
        pdf.drawString(res_x + (incremento_x * 6), res_y2, str(B_e))
        pdf.drawString(res_x + (incremento_x * 7), res_y2, str(Cl_e))
        pdf.drawString(res_x + (incremento_x * 8), res_y2, str(Cu_e))
        pdf.drawString(res_x + (incremento_x * 9), res_y2, str(Fe_e))
        pdf.drawString(res_x + (incremento_x * 10), res_y2, str(Mn_e))
        pdf.drawString(res_x + (incremento_x * 11), res_y2, str(Mo_e))
        pdf.drawString(res_x + (incremento_x * 12), res_y2, str(Zn_e))
        pdf.drawString(res_x + (incremento_x * 13), res_y2, str(Ni_e))

        # Impresión de valores Kg/Ha Existentes
        
        res_y3 = base_y - (inter * 9)
        pdf.drawString(res_x, res_y3, str(N_a))
        pdf.drawString(res_x + (incremento_x * 1), res_y3, str(P_a))
        pdf.drawString(res_x + (incremento_x * 2), res_y3, str(K_a))
        pdf.drawString(res_x + (incremento_x * 3), res_y3, str(Ca_a))
        pdf.drawString(res_x + (incremento_x * 4), res_y3, str(Mg_a))
        pdf.drawString(res_x + (incremento_x * 5), res_y3, str(S_a))
        pdf.drawString(res_x + (incremento_x * 6), res_y3, str(B_a))
        pdf.drawString(res_x + (incremento_x * 7), res_y3, str(Cl_a))
        pdf.drawString(res_x + (incremento_x * 8), res_y3, str(Cu_a))
        pdf.drawString(res_x + (incremento_x * 9), res_y3, str(Fe_a))
        pdf.drawString(res_x + (incremento_x * 10), res_y3, str(Mn_a))
        pdf.drawString(res_x + (incremento_x * 11), res_y3, str(Mo_a))
        pdf.drawString(res_x + (incremento_x * 12), res_y3, str(Zn_a))
        pdf.drawString(res_x + (incremento_x * 13), res_y3, str(Ni_a))

        # Rectangulos
        rec_x = base_x
        rec_y = base_y
        pdf.rect(rec_x, rec_y,550, -(inter*10))

        # Indicacion de N.D.
        pdf.drawString(res_x, res_y3-30, "*N.D. ==> No Determinado")


    def get(self,request,  pk, *args, **kwargs):
        analisis = get_object_or_404(ResultadosTotal, pk= pk)

        response = HttpResponse(content_type='application/pdf')
        # Para descargar el pdf con un nombre especifico
        #response['Content-Disposition'] = 'attachment; filename=prueba-lab.pdf'
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=letter)

        self.cabecera(pdf)
        self.titulo(pdf)
        self.informacionGeneral(pdf, analisis)
        self.page_2(pdf)
        self.bases_cambio(pdf, analisis)
        self.rel_bases_cambio(pdf, analisis)
        self.extracto_salinidad(pdf, analisis)
        self.aportacion_requ(pdf, analisis)
        pdf.showPage()

        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class ResultadosTotalListView(ListView):
    model = ResultadosTotal
    paginate_by = 10
    
    