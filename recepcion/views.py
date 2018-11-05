from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from .models import Recepcion
from generales.models import Municipio
from .forms import RecepcionForm

from reportes.models import ResultadosTotal
from django.conf import settings
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import datetime
from calculos.reportes import valor_str, valor_str_SD

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class RecepcionListView(ListView):
    model = Recepcion
    paginate_by = 10

@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class RecepcionCreateView(CreateView):
    model = Recepcion
    form_class = RecepcionForm
    success_url = reverse_lazy('recepcion:list')

@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class RecepcionUpdateView(UpdateView):
    model = Recepcion
    form_class = RecepcionForm
    success_url = reverse_lazy('recepcion:list')
    template_name_suffix = '_update_form'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class RecepcionDeleteView(DeleteView):
    model = Recepcion
    success_url = reverse_lazy('recepcion:list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class Reporte_Recepcion_PDF(View):

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
        pdf.drawString(165, 730, 'Recepción para Análisis Fisicoquimico de Suelo')

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

    def consulta_resultados(self, pdf, analisis):
        y = 500
        x = 40

        pdf.setFont('Helvetica', 12)
        pdf.drawString(x, y, "Podras consultar tus resultados 10 dias habiles posteriores a la fecha de recepción en la pagina:")
        pdf.setFillColorRGB(.1529,.1529,.8431)
        pdf.setFont('Helvetica-Bold', 12)
        pdf.drawString(x + 130, y - 25, "www.liaagrolaboratorio.com.mx/resultados")
        pdf.setFillColorRGB(0, 0, 0)
        pdf.setFont('Helvetica-Bold', 12)
        pdf.drawString(x + 150, y - 45, "Clave de Consulta: " +  analisis.slug)

    def get(self,request,  pk, *args, **kwargs):
        analisis = get_object_or_404(ResultadosTotal, folio_id= pk)

        response = HttpResponse(content_type='application/pdf')
        # Para descargar el pdf con un nombre especifico
        #response['Content-Disposition'] = 'attachment; filename=prueba-lab.pdf'
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=letter)

        self.cabecera(pdf)
        self.titulo(pdf)
        self.informacionGeneral(pdf, analisis)
        self.consulta_resultados(pdf, analisis)
        
        pdf.showPage()

        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response