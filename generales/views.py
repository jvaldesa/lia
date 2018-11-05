from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Analista, Cultivo, Estado, Municipio, Organizacion, RegimenHidrico, TipoAnalisis
from .forms import AnalistaForm, CultivoForm, EstadoForm, MunicipioForm, OrganizacionForm, RegimenHidricoForm, TipoAnalisisForm, SearchForm


from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Create your views here.

#-----ANALISTA------
@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class AnalistaCreateView(CreateView):
    model = Analista
    form_class = AnalistaForm
    success_url = reverse_lazy('generales:analista_list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class AnalistaUpdateView(UpdateView):
    model = Analista
    form_class = AnalistaForm
    template_name_suffix = '_form_update'
    success_url = reverse_lazy('generales:analista_list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class AnalistaListView(ListView):
    model = Analista


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class AnalistaDeleteView(DeleteView):
    model = Analista
    success_url = reverse_lazy('generales:analista_list')



#-----CULTIVO------
@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class CultivoCreateView(CreateView):
    model = Cultivo
    form_class = CultivoForm
    success_url = reverse_lazy('generales:cultivo_list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class CultivoUpdateView(UpdateView):
    model = Cultivo
    form_class = CultivoForm
    template_name_suffix = '_form_update'
    success_url = reverse_lazy('generales:cultivo_list')



@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class CultivoListView(ListView):
    model = Cultivo


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class CultivoDeleteView(DeleteView):
    model = Cultivo
    success_url = reverse_lazy('generales:cultivo_list')


#-----ESTADO------
@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class EstadoUpdateView(UpdateView):
    model = Estado
    form_class = EstadoForm
    template_name_suffix = '_form_update'
    success_url = reverse_lazy('generales:estado_list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class EstadoListView(ListView):
    model = Estado



#-----MUNICIPIO------
@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class MunicipioUpdateView(UpdateView):
    model = Municipio
    form_class = MunicipioForm
    template_name_suffix = '_form_update'
    success_url = reverse_lazy('generales:municipio_list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class MunicipioListView(ListView):
    model = Municipio
    # paginate_by = 15
    


#-----ORGANIZACION------
@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class OrganizacionCreateView(CreateView):
    model = Organizacion
    form_class = OrganizacionForm
    success_url = reverse_lazy('generales:organizacion_list')


def load_municipios(request):
    if not request.user.is_staff:
        return redirect(reverse_lazy('login'))
    else:
        estado_id = request.GET.get('estado')
        municipios = Municipio.objects.filter(estado_id=estado_id).order_by('nombre')
        return render(request, 'generales/municipio_dropdown_list_options.html', {'municipios': municipios})


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class OrganizacionUpdateView(UpdateView):
    model = Organizacion
    form_class = OrganizacionForm
    template_name_suffix = '_form_update'
    success_url = reverse_lazy('generales:organizacion_list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class OrganizacionListView(ListView):
    model = Organizacion


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class OrganizacionDetailView(DetailView):
    model = Organizacion
    template_name = 'generales/organizacion_detail.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class OrganizacionDeleteView(DeleteView):
    model = Organizacion
    success_url = reverse_lazy('generales:organizacion_list')



#-----REGIMEN HIDRICO------
@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class RegimenHidricoCreateView(CreateView):
    model = RegimenHidrico
    form_class = RegimenHidricoForm
    template_name = 'generales/regimen_hidrico_form.html'
    success_url = reverse_lazy('generales:regimen_hidrico_list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class RegimenHidricoUpdateView(UpdateView):
    model = RegimenHidrico
    form_class = RegimenHidricoForm
    template_name = 'generales/regimen_hidrico_form_update.html'
    success_url = reverse_lazy('generales:regimen_hidrico_list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class RegimenHidricoListView(ListView):
    model = RegimenHidrico
    template_name = 'generales/regimen_hidrico_list.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class RegimenHidricoDeleteView(DeleteView):
    model = RegimenHidrico
    success_url = reverse_lazy('generales:regimen_hidrico_list')
    template_name = 'generales/regimen_hidrico_confirm_delete.html'



#-----TIPO DE ANALISIS------
@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class TipoAnalisisCreateView(CreateView):
    model = TipoAnalisis
    form_class = TipoAnalisisForm
    template_name = 'generales/tipo_analisis_form.html'
    success_url = reverse_lazy('generales:tipo_analisis_list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class TipoAnalisisUpdateView(UpdateView):
    model = TipoAnalisis
    form_class = TipoAnalisisForm
    template_name = 'generales/tipo_analisis_form_update.html'
    success_url = reverse_lazy('generales:tipo_analisis_list')


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class TipoAnalisisListView(ListView):
    model = TipoAnalisis
    template_name = 'generales/tipo_analisis_list.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class TipoAnalisisDeleteView(DeleteView):
    model = TipoAnalisis
    success_url = reverse_lazy('generales:tipo_analisis_list')
    template_name = 'generales/tipo_analisis_confirm_delete.html'