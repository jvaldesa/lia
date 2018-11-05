from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import BasesCambio, RasPsi

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class BasesCambioListView(ListView):
    model = BasesCambio
    template_name = 'analisis_formula/bases_cambio_list.html'


@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class BasesCambioDetailView(DetailView):
    model = BasesCambio
    template_name = 'analisis_formula/bases_cambio_detail.html'
    
@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class RasPsiListView(ListView):
    model = RasPsi
    template_name = 'analisis_formula/ras_psi_list.html'

@method_decorator(staff_member_required(login_url='login'), name='dispatch')
class RasPsioDetailView(DetailView):
    model = RasPsi
    template_name = 'analisis_formula/ras_psi_detail.html'
    