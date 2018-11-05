from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import PhCePasta, Cationes, Aniones
from .forms import PhCePastaForm, PhCePastaFormUpdate, CationesForm, CationesFormUpdate, AnionesForm, AnionesFormUpdate
from calculos.salinidad import cationes as cal_cationes, aniones as cal_aniones

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Create your views here.


#----Ph Y CONDUCTIVIDAD ELECTRICA PASTA DE SATURACION
@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class PhCePastaCreateView(CreateView):
    model = PhCePasta
    form_class = PhCePastaForm
    template_name = 'analisis_salinidad/phCePasta_form.html'
    success_url = reverse_lazy('analisis_salinidad:phCePasta_list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class PhCePastaUpdateView(UpdateView):
    model = PhCePasta
    form_class = PhCePastaFormUpdate
    template_name = 'analisis_salinidad/phCePasta_update_form.html'
    success_url = reverse_lazy('analisis_salinidad:phCePasta_list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class PhCePastaDetailView(DetailView):
    model = PhCePasta
    template_name = 'analisis_salinidad/phCePasta_detail.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class PhCePastaListView(ListView):
    model = PhCePasta
    template_name = 'analisis_salinidad/phCePasta_list.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class PhCePastaDeleteView(DeleteView):
    model = PhCePasta
    template_name = 'analisis_salinidad/phCePasta_confirm_delete.html'
    success_url = reverse_lazy('analisis_salinidad:phCePasta_list')




#----CATIONES
def cationesCreate(request):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        form = CationesForm(request.POST or None)
        template = 'analisis_salinidad/cationes_form.html'

        if request.method == 'POST':
            if form.is_valid():
                folio = form.cleaned_data.get('folio')
                titulacionCaMg = form.cleaned_data.get('titulacionCaMg')
                normalidadEDTA = form.cleaned_data.get('normalidadEDTA')
                titulacionCa = form.cleaned_data.get('titulacionCa')
                alicuota = form.cleaned_data.get('alicuota')
                Na = form.cleaned_data.get('Na')
                K = form.cleaned_data.get('K')
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')

                cationes_res = cal_cationes(titulacionCaMg, normalidadEDTA, titulacionCa, alicuota, Na, K)
                CaCation = cationes_res['Ca']
                MgCation = cationes_res['Mg']
                NaCation = cationes_res['Na']
                KCation = cationes_res['K']

                obj = Cationes.objects.create(
                    folio = folio,
                    titulacionCaMg = titulacionCaMg,
                    normalidadEDTA = normalidadEDTA,
                    titulacionCa = titulacionCa,
                    alicuota = alicuota,
                    Na = Na,
                    K = K,
                    CaCation = CaCation,
                    MgCation = MgCation,
                    NaCation = NaCation,
                    KCation = KCation,
                    analista = analista,
                    fecha_analisis = fecha_analisis,
                )

                registro = Cationes.objects.get(folio=folio)
                template = 'analisis_salinidad/cationes_detail.html'
                return render(request, template, {'object':registro})


        contexto = {
            'form':form,
        }

        return render(request, template, contexto)


def cationesUpdate(request, pk=None):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        registro = get_object_or_404(Cationes, pk=pk)
        form = CationesFormUpdate(request.POST or None, instance=registro)
        template = 'analisis_salinidad/cationes_update_form.html'

        if request.method == 'POST':
            if form.is_valid():
                folio = form.cleaned_data.get('folio')
                titulacionCaMg = form.cleaned_data.get('titulacionCaMg')
                normalidadEDTA = form.cleaned_data.get('normalidadEDTA')
                titulacionCa = form.cleaned_data.get('titulacionCa')
                alicuota = form.cleaned_data.get('alicuota')
                Na = form.cleaned_data.get('Na')
                K = form.cleaned_data.get('K')
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')

                cationes_res = cal_cationes(titulacionCaMg, normalidadEDTA, titulacionCa, alicuota, Na, K)
                CaCation = cationes_res['Ca']
                MgCation = cationes_res['Mg']
                NaCation = cationes_res['Na']
                KCation = cationes_res['K']

                registro.folio = folio
                registro.titulacionCaMg = titulacionCaMg
                registro.normalidadEDTA = normalidadEDTA
                registro.titulacionCa = titulacionCa
                registro.alicuota = alicuota
                registro.Na = Na
                registro.K = K
                registro.CaCation = CaCation
                registro.MgCation = MgCation
                registro.NaCation = NaCation
                registro.KCation = KCation
                registro.analista = analista
                registro.fecha_analisis = fecha_analisis

                registro.save()
                template = 'analisis_salinidad/cationes_detail.html'
                return render(request, template, {'object':registro})

        contexto = {
            'object': registro,
            'form':form,
        }

        return render(request, template, contexto)


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class CationesDetailView(DetailView):
    model = Cationes
    template_name = 'analisis_salinidad/cationes_detail.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class CationesListView(ListView):
    model = Cationes
    template_name = 'analisis_salinidad/cationes_list.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class CationesDeleteView(DeleteView):
    model = Cationes
    template_name = 'analisis_salinidad/cationes_confirm_delete.html'
    success_url = reverse_lazy('analisis_salinidad:cationes_list')




#----ANIONES
def anionesCreate(request):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        form = AnionesForm(request.POST or None)
        template = 'analisis_salinidad/aniones_form.html'

        if request.method == 'POST':
            if form.is_valid():
                folio = form.cleaned_data.get('folio')
                titulacionCar = form.cleaned_data.get('titulacionCar')
                titulacionBlancoCar = form.cleaned_data.get('titulacionBlancoCar')
                normalidadH2SO4 = form.cleaned_data.get('normalidadH2SO4')
                alicuotaCar = form.cleaned_data.get('alicuotaCar')
                titulacionBic = form.cleaned_data.get('titulacionBic')
                titulacionBlancoBic = form.cleaned_data.get('titulacionBlancoBic')
                alicuotaBic = form.cleaned_data.get('alicuotaBic')
                titulacionClo = form.cleaned_data.get('titulacionClo')
                titulacionBlancoClo = form.cleaned_data.get('titulacionBlancoClo')
                normalidadAgNO3 = form.cleaned_data.get('normalidadAgNO3')
                alicuotaClo = form.cleaned_data.get('alicuotaClo')
                conductividadEl = form.cleaned_data.get('conductividadEl')
                unidad = form.cleaned_data.get('unidad')
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')

                res_aniones = cal_aniones(titulacionCar, titulacionBlancoCar, normalidadH2SO4, alicuotaCar, titulacionBic, titulacionBlancoBic, alicuotaBic, titulacionClo, titulacionBlancoClo, normalidadAgNO3, alicuotaClo, conductividadEl, unidad)

                carbonatos = res_aniones['Carbonatos']
                bicarbonatos = res_aniones['Bicarbonatos']
                cloruros = res_aniones['Cloruros']
                sulfatos = res_aniones['Sulfatos']

                obj = Aniones.objects.create(
                    folio = folio,
                    titulacionCar = titulacionCar,
                    titulacionBlancoCar = titulacionBlancoCar,
                    normalidadH2SO4 = normalidadH2SO4,
                    alicuotaCar = alicuotaCar,
                    titulacionBic = titulacionBic,
                    titulacionBlancoBic = titulacionBlancoBic,
                    alicuotaBic = alicuotaBic,
                    titulacionClo = titulacionClo,
                    titulacionBlancoClo = titulacionBlancoClo,
                    normalidadAgNO3 = normalidadAgNO3,
                    alicuotaClo = alicuotaClo,
                    conductividadEl = conductividadEl,
                    unidad = unidad,
                    carbonatos = carbonatos,
                    bicarbonatos = bicarbonatos,
                    cloruros = cloruros,
                    sulfatos = sulfatos,
                    analista = analista,
                    fecha_analisis = fecha_analisis,
                )

                registro = Aniones.objects.get(folio=folio)
                template = 'analisis_salinidad/aniones_detail.html'
                return render(request, template, {'object':registro})


        contexto = {
            'form':form,
        }

        return render(request, template, contexto)


def anionesUpdate(request, pk=None):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        registro = get_object_or_404(Aniones, pk=pk)
        form = AnionesFormUpdate(request.POST or None, instance=registro)
        template = 'analisis_salinidad/aniones_update_form.html'

        if request.method == 'POST':
            if form.is_valid():
                folio = form.cleaned_data.get('folio')
                titulacionCar = form.cleaned_data.get('titulacionCar')
                titulacionBlancoCar = form.cleaned_data.get('titulacionBlancoCar')
                normalidadH2SO4 = form.cleaned_data.get('normalidadH2SO4')
                alicuotaCar = form.cleaned_data.get('alicuotaCar')
                titulacionBic = form.cleaned_data.get('titulacionBic')
                titulacionBlancoBic = form.cleaned_data.get('titulacionBlancoBic')
                alicuotaBic = form.cleaned_data.get('alicuotaBic')
                titulacionClo = form.cleaned_data.get('titulacionClo')
                titulacionBlancoClo = form.cleaned_data.get('titulacionBlancoClo')
                normalidadAgNO3 = form.cleaned_data.get('normalidadAgNO3')
                alicuotaClo = form.cleaned_data.get('alicuotaClo')
                conductividadEl = form.cleaned_data.get('conductividadEl')
                unidad = form.cleaned_data.get('unidad')
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')

                res_aniones = cal_aniones(titulacionCar, titulacionBlancoCar, normalidadH2SO4, alicuotaCar, titulacionBic, titulacionBlancoBic, alicuotaBic, titulacionClo, titulacionBlancoClo, normalidadAgNO3, alicuotaClo, conductividadEl, unidad)

                carbonatos = res_aniones['Carbonatos']
                bicarbonatos = res_aniones['Bicarbonatos']
                cloruros = res_aniones['Cloruros']
                sulfatos = res_aniones['Sulfatos']

                registro.folio = folio
                registro.titulacionCar = titulacionCar
                registro.titulacionBlancoCar = titulacionBlancoCar
                registro.normalidadH2SO4 = normalidadH2SO4
                registro.alicuotaCar = alicuotaCar
                registro.titulacionBic = titulacionBic
                registro.titulacionBlancoBic = titulacionBlancoBic
                registro.alicuotaBic = alicuotaBic
                registro.titulacionClo = titulacionClo
                registro.titulacionBlancoClo = titulacionBlancoClo
                registro.normalidadAgNO3 = normalidadAgNO3
                registro.alicuotaClo = alicuotaClo
                registro.conductividadEl = conductividadEl
                registro.unidad = unidad
                registro.carbonatos = carbonatos
                registro.bicarbonatos = bicarbonatos
                registro.cloruros = cloruros
                registro.sulfatos = sulfatos
                registro.analista = analista
                registro.fecha_analisis = fecha_analisis

                registro.save()
                template = 'analisis_salinidad/aniones_detail.html'
                return render(request, template, {'object':registro})

        contexto = {
            'object': registro,
            'form':form,
        }

        return render(request, template, contexto)


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class AnionesDetailView(DetailView):
    model = Aniones
    template_name = 'analisis_salinidad/aniones_detail.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class AnionesListView(ListView):
    model = Aniones
    template_name = 'analisis_salinidad/aniones_list.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class AnionesDeleteView(DeleteView):
    model = Aniones
    template_name = 'analisis_salinidad/aniones_confirm_delete.html'
    success_url = reverse_lazy('analisis_salinidad/aniones_list.html')