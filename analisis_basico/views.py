from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Textura, Ph_ConductividadElectrica, MateriaOrganica, ColorDensidadAparente, PuntoSaturacion
from .forms import TexturaForm, ConsultaForm, TexturaFormUpdate, PhyCeForm, PhyCeFormUpdate, MateriaOrganicaForm, MateriaOrganicaFormUpdate, ColorDensidadAparenteForm, ColorDensidadAparenteFormUpdate, PuntoSaturacionForm, PuntoSaturacionFormUpdate
from calculos.basico import textura as cal_textura, ph as cal_ph, conductividadElectrica, materiaOrganica as cal_MO, densidadAparente as cal_DA, puntoSaturacion as cal_PS
from recepcion.models import Recepcion

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
# Create your views here.


#----TEXTURA

def texturaCreate(request):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        form = TexturaForm(request.POST or None)
        if request.method == 'POST':
            
            if form.is_valid():
                if form.cleaned_data.get('textura') == None:
                    folio = form.cleaned_data.get('folio')
                    l1 = form.cleaned_data.get('lectura_1')
                    l2 = form.cleaned_data.get('lectura_2')
                    l3 = form.cleaned_data.get('lectura_3')
                    l4 = form.cleaned_data.get('lectura_4')
                    t1 = form.cleaned_data.get('temperatura_1')
                    t2 = form.cleaned_data.get('temperatura_2')
                    t3 = form.cleaned_data.get('temperatura_3')
                    t4 = form.cleaned_data.get('temperatura_4')
                    analista = form.cleaned_data.get('analista')
                    fecha_analisis = form.cleaned_data.get('fecha_analisis')
                    textura_res = cal_textura(l1, l2, l3, l4, t1, t2, t3, t4)
                    arenas = textura_res['arenas']
                    arcillas = textura_res['arcillas']
                    limos = textura_res['limos']
                    textura = textura_res['textura']
                    obj = Textura.objects.create(
                        folio = folio,
                        lectura_1 = l1,
                        lectura_2 = l2,
                        lectura_3 = l3,
                        lectura_4 = l4,
                        temperatura_1 = t1,
                        temperatura_2 = t2,
                        temperatura_3 = t3,
                        temperatura_4 = t4,
                        arenas =  arenas,
                        arcillas = arcillas,
                        limos = limos,
                        textura = textura,
                        analista = analista,
                        fecha_analisis = fecha_analisis,
                    )
                    registro = Textura.objects.get(folio=folio)
                    form_ret = TexturaForm(instance=registro)
                    return render(request, 'analisis_basico/textura_detail.html', {'textura':registro})
            
        return render(request, 'analisis_basico/textura_form.html', {'form':form} )


def texturaUpdate(request, pk=None):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        registro = get_object_or_404(Textura, pk=pk)
        form = TexturaFormUpdate(request.POST or None, instance=registro)
        template = 'analisis_basico/textura_update_form.html'
        if request.method == 'POST':
            if form.is_valid():
                folio = form.cleaned_data.get('folio')
                l1 = form.cleaned_data.get('lectura_1')
                l2 = form.cleaned_data.get('lectura_2')
                l3 = form.cleaned_data.get('lectura_3')
                l4 = form.cleaned_data.get('lectura_4')
                t1 = form.cleaned_data.get('temperatura_1')
                t2 = form.cleaned_data.get('temperatura_2')
                t3 = form.cleaned_data.get('temperatura_3')
                t4 = form.cleaned_data.get('temperatura_4')
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')
                textura_res = cal_textura(l1, l2, l3, l4, t1, t2, t3, t4)
                arenas = textura_res['arenas']
                arcillas = textura_res['arcillas']
                limos = textura_res['limos']
                textura = textura_res['textura']

                registro.folio = folio
                registro.lectura_1 = l1
                registro.lectura_2 = l2
                registro.lectura_3 = l3
                registro.lectura_4 = l4
                registro.temperatura_1 = t1
                registro.temperatura_2 = t2
                registro.temperatura_3 = t3
                registro.temperatura_4 = t4
                registro.arenas = arenas
                registro.arcillas = arcillas
                registro.limos = limos
                registro.textura = textura
                registro.analista = analista
                registro.fecha_analisis = fecha_analisis

                registro.save()
                return render(request, 'analisis_basico/textura_detail.html', {'textura':registro})

        context = {
            'object': registro,
            'form': form
        }
        
        return render(request, template, context)
        

@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class TexturaDetailView(DetailView):
    model = Textura


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class TexturaListView(ListView):
    model = Textura


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class TexturaDeleteView(DeleteView):
    model = Textura
    success_url = reverse_lazy('analisis_basico:textura_list')



#----Ph Y CONDUCTIVIDAD ELECTRICA
def PhCeCreate(request):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        form = PhyCeForm(request.POST or None)
        if request.method == 'POST':
            
            if form.is_valid():
                folio = form.cleaned_data.get('folio')
                ph = form.cleaned_data.get('ph')
                ce = form.cleaned_data.get('ce')
                unidad = form.cleaned_data.get('unidad')
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')
                ph_clasificacion = cal_ph(ph)
                ce_clasificacion = conductividadElectrica(ce, unidad)
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')
                obj = Ph_ConductividadElectrica.objects.create(
                    folio = folio,
                    ph = ph,
                    clasificacion_ph = ph_clasificacion,
                    ce = ce,
                    unidad = unidad,
                    clasificacion_ce = ce_clasificacion,
                    analista = analista,
                    fecha_analisis = fecha_analisis,
                )
                registro = Ph_ConductividadElectrica.objects.get(folio=folio)
                return render(request, 'analisis_basico/ph_ce_detail.html', {'object':registro})
        
        return render(request, 'analisis_basico/ph_ce_form.html', {'form':form})


def PhCeUpdate(request, pk=None):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        registro = get_object_or_404(Ph_ConductividadElectrica, pk=pk)
        form = PhyCeFormUpdate(request.POST or None, instance=registro)
        template = 'analisis_basico/ph_ce_update_form.html'
        if request.method == 'POST':
            
            if form.is_valid():
                folio = form.cleaned_data.get('folio')
                ph = form.cleaned_data.get('ph')
                ce = form.cleaned_data.get('ce')
                unidad = form.cleaned_data.get('unidad')
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')
                ph_clasificacion = cal_ph(ph)
                ce_clasificacion = conductividadElectrica(ce, unidad)
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')
                
                registro.folio = folio
                registro.ph = ph
                registro.clasificacion_ph = ph_clasificacion
                registro.ce = ce
                registro.unidad = unidad
                registro.clasificacion_ce = ce_clasificacion
                registro.analista = analista
                registro.fecha_analisis = fecha_analisis

                registro.save()
                return render(request, 'analisis_basico/ph_ce_detail.html', {'object':registro})
        context = {
            'object':registro,
            'form':form
        }
        
        return render(request, template, context)


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class PhCeDetailView(DetailView):
    model = Ph_ConductividadElectrica
    template_name = 'analisis_basico/ph_ce_detail.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class PhCeListView(ListView):
    model = Ph_ConductividadElectrica
    template_name = 'analisis_basico/ph_ce_list.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class PhCeDeleteView(DeleteView):
    model = Ph_ConductividadElectrica
    success_url = reverse_lazy('analisis_basico:ph_ce_list')
    template_name = 'analisis_basico/ph_ce_confirm_delete.html'



#----MATERIA ORGANICA
def materiaOrganicaCreate(request):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        form = MateriaOrganicaForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                folio = form.cleaned_data.get('folio')
                clase_suelo = form.cleaned_data.get('clase_suelo')
                b1 = form.cleaned_data.get('b1')
                b2 = form.cleaned_data.get('b2')
                b3 = form.cleaned_data.get('b3')
                t = form.cleaned_data.get('t')
                g = form.cleaned_data.get('g')
                N = form.cleaned_data.get('N')
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')

                res_MO = cal_MO(clase_suelo, b1, b2, b3, t, g, N)
                Mo = res_MO['MO']
                interpretacion = res_MO['clasificacion']

                obj = MateriaOrganica.objects.create(
                    folio = folio,
                    clase_suelo = clase_suelo,
                    b1 = b1,
                    b2 = b2,
                    b3 = b3,
                    t = t,
                    g = g,
                    N = N,
                    materia_organica = Mo,
                    interpretacion = interpretacion,
                    analista = analista,
                    fecha_analisis = fecha_analisis,
                )

                registro = MateriaOrganica.objects.get(folio=folio)
                return render(request, 'analisis_basico/materia_organica_detail.html', {'object':registro})
        return render(request, 'analisis_basico/materia_organica_form.html', {'form':form})

def materiaOrganicaUpdate(request, pk=None):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        registro = get_object_or_404(MateriaOrganica, pk=pk)
        form = MateriaOrganicaFormUpdate(request.POST or None, instance=registro)
        template = 'analisis_basico/materia_organica_update_form.html'

        if request.method == 'POST':
            if form.is_valid():
                folio = form.cleaned_data.get('folio')
                clase_suelo = form.cleaned_data.get('clase_suelo')
                b1 = form.cleaned_data.get('b1')
                b2 = form.cleaned_data.get('b2')
                b3 = form.cleaned_data.get('b3')
                t = form.cleaned_data.get('t')
                g = form.cleaned_data.get('g')
                N = form.cleaned_data.get('N')
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')

                res_MO = cal_MO(clase_suelo, b1, b2, b3, t, g, N)
                Mo = res_MO['MO']
                interpretacion = res_MO['clasificacion']

                registro.folio = folio
                registro.clase_suelo = clase_suelo
                registro.b1 = b1
                registro.b2 = b2
                registro.b3 = b3
                registro.t = t
                registro.g = g
                registro.N = N
                registro.materia_organica = Mo
                registro.interpretacion = interpretacion
                registro.analista = analista
                registro.fecha_analisis = fecha_analisis

                registro.save()
                return render(request, 'analisis_basico/materia_organica_detail.html', {'object':registro})

        context = {
            'object':registro,
            'form':form
        }

        return render(request, template, context)


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class MateriaOrganicaDetailView(DetailView):
    model = MateriaOrganica
    template_name = 'analisis_basico/materia_organica_detail.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class MateriaOrganicaListView(ListView):
    model = MateriaOrganica
    template_name = 'analisis_basico/materia_organica_list.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class MateriaOrganicaDeleteView(DeleteView):
    model = MateriaOrganica
    success_url = reverse_lazy('analisis_basico:materia_organica_list')
    template_name = 'analisis_basico/materia_organica_confirm_delete.html'




#----COLOR Y DENSIDAD APARENTE
def colorDensidadAparenteCreate(request):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        form = ColorDensidadAparenteForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                folio = form.cleaned_data.get('folio')
                clave = form.cleaned_data.get('clave')
                color = form.cleaned_data.get('color')
                peso = form.cleaned_data.get('peso')
                volumen = form.cleaned_data.get('volumen')
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')

                res_DA = cal_DA(peso, volumen)

                obj = ColorDensidadAparente.objects.create(
                    folio = folio,
                    clave = clave,
                    color = color,
                    peso = peso,
                    volumen = volumen,
                    densidad_aparente = res_DA,
                    analista = analista,
                    fecha_analisis = fecha_analisis,
                )

                registro = ColorDensidadAparente.objects.get(folio=folio)
                return render(request, 'analisis_basico/color_densidad_aparente_detail.html', {'object': registro})
        
        return render(request, 'analisis_basico/color_densidad_aparente_form.html', {'form': form})


def colorDensidadAparenteUpdate(request, pk=None):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        registro = get_object_or_404(ColorDensidadAparente, pk=pk)
        form = ColorDensidadAparenteFormUpdate(request.POST or None, instance=registro)
        template = 'analisis_basico/color_densidad_aparente_update_form.html'
        if request.method == 'POST':
            if form.is_valid():
                folio = form.cleaned_data.get('folio')
                clave = form.cleaned_data.get('clave')
                color = form.cleaned_data.get('color')
                peso = form.cleaned_data.get('peso')
                volumen = form.cleaned_data.get('volumen')
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')

                res_DA = cal_DA(peso, volumen)

                registro.folio = folio
                registro.clave = clave
                registro.color = color
                registro.peso = peso
                registro.volumen = volumen
                registro.densidad_aparente = res_DA
                registro.analista = analista
                registro.fecha_analisis = fecha_analisis

                registro.save()
                return render(request, 'analisis_basico/color_densidad_aparente_detail.html', {'object':registro})

        context = {
            'object':registro,
            'form':form
        }

        return render(request, template, context)


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class ColorDensidadAparenteDetailView(DetailView):
    model = ColorDensidadAparente
    template_name = 'analisis_basico/color_densidad_aparente_detail.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class ColorDensidadAparenteListView(ListView):
    model = ColorDensidadAparente
    template_name = 'analisis_basico/color_densidad_aparente_list.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class ColorDensidadAparenteDeleteView(DeleteView):
    model = ColorDensidadAparente
    template_name = 'analisis_basico/color_densidad_aparente_confirm_delete.html'
    success_url = reverse_lazy('analisis_basico:color_densidad_aparente_list')




#----PUNTO DE SATURACION
def puntoSaturacionCreate(request):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        form = PuntoSaturacionForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                folio = form.cleaned_data.get('folio')
                peso_inicial_estufa = form.cleaned_data.get('peso_inicial_estufa')
                peso_final_estufa = form.cleaned_data.get('peso_final_estufa')
                agua_gastada_estufa = form.cleaned_data.get('agua_gastada_estufa')
                peso_inicial_aire = form.cleaned_data.get('peso_inicial_aire')
                peso_final_aire = form.cleaned_data.get('peso_final_aire')
                agua_gastada_aire = form.cleaned_data.get('agua_gastada_aire')
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')

                res_PS = cal_PS(peso_inicial_estufa, peso_final_estufa, agua_gastada_estufa, peso_inicial_aire, peso_final_aire, agua_gastada_aire)
                punto_saturacion = res_PS['PS']
                capacidad_campo = res_PS['CC']
                punto_marchitez = res_PS['PMP']

                obj = PuntoSaturacion.objects.create(
                    folio = folio,
                    peso_inicial_estufa = peso_inicial_estufa,
                    peso_final_estufa =  peso_final_estufa,
                    agua_gastada_estufa =  agua_gastada_estufa,
                    peso_inicial_aire =  peso_inicial_aire,
                    peso_final_aire =  peso_final_aire,
                    agua_gastada_aire =  agua_gastada_aire,
                    punto_saturacion =  punto_saturacion,
                    capacidad_campo =  capacidad_campo,
                    punto_marchitez =  punto_marchitez,
                    analista = analista,
                    fecha_analisis = fecha_analisis,
                )
                registro = PuntoSaturacion.objects.get(folio=folio)
                return render(request, 'analisis_basico/punto_saturacion_detail.html', {'object':registro})
        return render(request, 'analisis_basico/punto_saturacion_form.html', {'form':form})


    

def puntoSaturacionUpdate(request, pk=None):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        registro = get_object_or_404(PuntoSaturacion, pk=pk)
        form = PuntoSaturacionFormUpdate(request.POST or None, instance=registro)
        template = 'analisis_basico/punto_saturacion_update_form.html'

        if request.method == 'POST':
            if form.is_valid():
                folio = form.cleaned_data.get('folio')
                peso_inicial_estufa = form.cleaned_data.get('peso_inicial_estufa')
                peso_final_estufa = form.cleaned_data.get('peso_final_estufa')
                agua_gastada_estufa = form.cleaned_data.get('agua_gastada_estufa')
                peso_inicial_aire = form.cleaned_data.get('peso_inicial_aire')
                peso_final_aire = form.cleaned_data.get('peso_final_aire')
                agua_gastada_aire = form.cleaned_data.get('agua_gastada_aire')
                analista = form.cleaned_data.get('analista')
                fecha_analisis = form.cleaned_data.get('fecha_analisis')

                res_PS = cal_PS(peso_inicial_estufa, peso_final_estufa, agua_gastada_estufa, peso_inicial_aire, peso_final_aire, agua_gastada_aire)
                punto_saturacion = res_PS['PS']
                capacidad_campo = res_PS['CC']
                punto_marchitez = res_PS['PMP']

                registro.folio = folio
                registro.peso_inicial_estufa = peso_inicial_estufa
                registro.peso_final_estufa =  peso_final_estufa
                registro.agua_gastada_estufa =  agua_gastada_estufa
                registro.peso_inicial_aire =  peso_inicial_aire
                registro.peso_final_aire =  peso_final_aire
                registro.agua_gastada_aire =  agua_gastada_aire
                registro.punto_saturacion =  punto_saturacion
                registro.capacidad_campo =  capacidad_campo
                registro.punto_marchitez =  punto_marchitez
                registro.analista = analista
                registro.fecha_analisis = fecha_analisis

                registro.save()
                return render(request, 'analisis_basico/punto_saturacion_detail.html', {'object':registro})
        context = {
            'object':registro,
            'form':form
        }
        
        return render(request, template, context)


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class PuntoSaturacionDetailView(DetailView):
    model = PuntoSaturacion
    template_name = 'analisis_basico/punto_saturacion_detail.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class PuntoSaturacionListView(ListView):
    model = PuntoSaturacion
    template_name = 'analisis_basico/punto_saturacion_list.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class PuntoSaturacionDeleteView(DeleteView):
    model = PuntoSaturacion
    success_url = reverse_lazy('analisis_basico:punto_saturacion_list')
    template_name = 'analisis_basico/punto_saturacion_confirm_delete.html'













    
#Prueba para hacer consultas
def consulta(request):
    form = ConsultaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            folio = form.cleaned_data.get('folio')
            print(folio)
            recepcion = Recepcion.objects.get(folio=folio)
            print(recepcion)
            id_folio = recepcion.pk
            print(id_folio)
            texturaq = Textura.objects.get(folio=id_folio)
            contexto = {'recepcion':recepcion, 'textura':texturaq}
            return render(request, 'analisis_basico/resultados.html', contexto)


    return render(request, 'analisis_basico/consulta_form.html', {'form':form})
