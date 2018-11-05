from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Nitrogeno, CarbonatosTotales, Micronutrientes, BasesIntercambiables, Fosforo
from calculos.nutrientes import nitrogeno as cal_nitrogeno, carbonatos as cal_carbonatos
from .forms import (
    NitrogenoForm, NitrogenoFormUpdate,
    CarbonatosTotalesForm, CarbonatosTotalesFormUpdate,
    MicronutrientesForm, MicronutrientesFormUpdate,
    BasesIntercambiablesForm, BasesIntercambiablesFormUpdate,
    FosforoForm, FosforoFormUpdate,
    )

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


# Create your views here.

#----NITROGENO
def nitrogenoCreate(request):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        form = NitrogenoForm(request.POST or None)
        template = 'analisis_nutrientes/nitrogeno_form.html'

        if request.method == 'POST':
            if form.is_valid():
                folio = form.cleaned_data.get('folio')
                M = form.cleaned_data.get('M')
                B = form.cleaned_data.get('B')
                N = form.cleaned_data.get('N')
                Vi = form.cleaned_data.get('Vi')
                a = form.cleaned_data.get('a')
                p = form.cleaned_data.get('p')
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')

                nitrogeno_res = cal_nitrogeno(M, B, N, Vi, a, p)
                nitrogeno = nitrogeno_res

                obj = Nitrogeno.objects.create(
                    folio = folio,
                    M = M,
                    B = B,
                    N = N,
                    Vi = Vi,
                    a = a,
                    p = p,
                    nitrogeno = nitrogeno,
                    analista = analista,
                    fecha_analisis = fecha_analisis,
                )

                registro = Nitrogeno.objects.get(folio=folio)
                template = 'analisis_nutrientes/nitrogeno_detail.html'
                return render(request, template, {'object':registro})


        contexto = {
            'form':form,
        }

        return render(request, template, contexto)


def nitrogenoUpdate(request, pk=None):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        registro = get_object_or_404(Nitrogeno, pk=pk)
        form = NitrogenoFormUpdate(request.POST or None, instance=registro)
        template = 'analisis_nutrientes/nitrogeno_update_form.html'

        if request.method == 'POST':
            if form.is_valid():
                folio = form.cleaned_data.get('folio')
                M = form.cleaned_data.get('M')
                B = form.cleaned_data.get('B')
                N = form.cleaned_data.get('N')
                Vi = form.cleaned_data.get('Vi')
                a = form.cleaned_data.get('a')
                p = form.cleaned_data.get('p')
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')

                nitrogeno_res = cal_nitrogeno(M, B, N, Vi, a, p)
                nitrogeno = nitrogeno_res

                registro.folio = folio
                registro.M = M
                registro.B = B
                registro.N = N
                registro.Vi = Vi
                registro.a = a
                registro.p = p
                registro.nitrogeno = nitrogeno
                registro.analista = analista
                registro.fecha_analisis = fecha_analisis

                registro.save()
                template = 'analisis_nutrientes/nitrogeno_detail.html'
                return render(request, template, {'object':registro})

        contexto = {
            'object': registro,
            'form':form,
        }

        return render(request, template, contexto)


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class NitrogenoDetailView(DetailView):
    model = Nitrogeno
    template_name = 'analisis_nutrientes/nitrogeno_detail.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class NitrogenoListView(ListView):
    model = Nitrogeno
    template_name = 'analisis_nutrientes/nitrogeno_list.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class NitrogenoDeleteView(DeleteView):
    model = Nitrogeno
    template_name = 'analisis_nutrientes/nitrogeno_confirm_delete.html'
    success_url = reverse_lazy('analisis_nutrientes/nitrogeno_list.html')



#----CARBONATOS TOTALES
def carbonatosCreate(request):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        form = CarbonatosTotalesForm(request.POST or None)
        template = 'analisis_nutrientes/carbonatos_form.html'

        if request.method == 'POST':
            if form.is_valid():
                folio = form.cleaned_data.get('folio')
                m = form.cleaned_data.get('m')
                a = form.cleaned_data.get('a')
                b = form.cleaned_data.get('b')
                s = form.cleaned_data.get('s')
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')

                res_carbonatos = cal_carbonatos(m, a, b, s)
                CaCo3 = res_carbonatos

                obj = CarbonatosTotales.objects.create(
                    folio = folio,
                    m = m,
                    a = a,
                    b = b,
                    s = s,
                    CaCo3 = CaCo3,
                    analista = analista,
                    fecha_analisis = fecha_analisis,
                )

                registro = CarbonatosTotales.objects.get(folio=folio)
                template = 'analisis_nutrientes/carbonatos_detail.html'
                return render(request, template, {'object':registro})


        contexto = {
            'form':form,
        }

        return render(request, template, contexto)


def carbonatosUpdate(request, pk=None):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        registro = get_object_or_404(CarbonatosTotales, pk=pk)
        form = CarbonatosTotalesFormUpdate(request.POST or None, instance=registro)
        template = 'analisis_nutrientes/carbonatos_update_form.html'

        if request.method == 'POST':
            if form.is_valid():
                folio = form.cleaned_data.get('folio')
                m = form.cleaned_data.get('m')
                a = form.cleaned_data.get('a')
                b = form.cleaned_data.get('b')
                s = form.cleaned_data.get('s')
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')

                res_carbonatos = cal_carbonatos(m, a, b, s)
                CaCo3 = res_carbonatos

                registro.folio = folio
                registro.m = m
                registro.a = a
                registro.b = b
                registro.s = s
                registro.CaCo3 = CaCo3
                registro.analista = analista
                registro.fecha_analisis = fecha_analisis

                registro.save()
                template = 'analisis_nutrientes/carbonatos_detail.html'
                return render(request, template, {'object':registro})

        contexto = {
            'object': registro,
            'form':form,
        }

        return render(request, template, contexto)


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class CarbonatosDetailView(DetailView):
    model = CarbonatosTotales
    template_name = 'analisis_nutrientes/carbonatos_detail.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class CarbonatosListView(ListView):
    model = CarbonatosTotales
    template_name = 'analisis_nutrientes/carbonatos_list.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class CarbonatosDeleteView(DeleteView):
    model = CarbonatosTotales
    template_name = 'analisis_nutrientes/carbonatos_confirm_delete.html'
    success_url = reverse_lazy('analisis_nutrientes/carbonatos_list.html')



#----MICRONUTRIENTES
@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class MicronutrientesCreateView(CreateView):
    model = Micronutrientes
    form_class = MicronutrientesForm
    template_name = 'analisis_nutrientes/micronutrientes_form.html'
    success_url = reverse_lazy('analisis_nutrientes:micronutrientes_list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class MicronutrientesUpdateView(UpdateView):
    model = Micronutrientes
    form_class = MicronutrientesFormUpdate
    template_name = 'analisis_nutrientes/micronutrientes_update_form.html'
    success_url = reverse_lazy('analisis_nutrientes:micronutrientes_list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class MicronutrientesDetailView(DetailView):
    model = Micronutrientes
    template_name = 'analisis_nutrientes/micronutrientes_detail.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class MicronutrientesListView(ListView):
    model = Micronutrientes
    template_name = 'analisis_nutrientes/micronutrientes_list.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class MicronutrientesDeleteView(DeleteView):
    model = Micronutrientes
    template_name = 'analisis_nutrientes/micronutrientes_confirm_delete.html'
    success_url = reverse_lazy('analisis_nutrientes:micronutrientes_list')



#----BASES INTERCAMBIABLES
@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class BasesIntercambiablesCreateView(CreateView):
    model = BasesIntercambiables
    form_class = BasesIntercambiablesForm
    template_name = 'analisis_nutrientes/bases_intercambiables_form.html'
    success_url = reverse_lazy('analisis_nutrientes:bases_intercambiables_list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class BasesIntercambiablesUpdateView(UpdateView):
    model = BasesIntercambiables
    form_class = BasesIntercambiablesFormUpdate
    template_name = 'analisis_nutrientes/bases_intercambiables_update_form.html'
    success_url = reverse_lazy('analisis_nutrientes:bases_intercambiables_list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class BasesIntercambiablesDetailView(DetailView):
    model = BasesIntercambiables
    template_name = 'analisis_nutrientes/bases_intercambiables_detail.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class BasesIntercambiablesListView(ListView):
    model = BasesIntercambiables
    template_name = 'analisis_nutrientes/bases_intercambiables_list.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class BasesIntercambiablesDeleteView(DeleteView):
    model = BasesIntercambiables
    template_name = 'analisis_nutrientes/bases_intercambiables_confirm_delete.html'
    success_url = reverse_lazy('analisis_nutrientes:bases_intercambiables_list')



#----FOSFORO
@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class FosforoCreateView(CreateView):
    model = Fosforo
    form_class = FosforoForm
    template_name = 'analisis_nutrientes/fosforo_form.html'
    success_url = reverse_lazy('analisis_nutrientes:fosforo_list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class FosforoUpdateView(UpdateView):
    model = Fosforo
    form_class = FosforoFormUpdate
    template_name = 'analisis_nutrientes/fosforo_update_form.html'
    success_url = reverse_lazy('analisis_nutrientes:fosforo_list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class FosforoDetailView(DetailView):
    model = Fosforo
    template_name = 'analisis_nutrientes/fosforo_detail.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class FosforoListView(ListView):
    model = Fosforo
    template_name = 'analisis_nutrientes/fosforo_list.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class FosforoDeleteView(DeleteView):
    model = Fosforo
    template_name = 'analisis_nutrientes/fosforo_confirm_delete.html'
    success_url = reverse_lazy('analisis_nutrientes:fosforo_list')