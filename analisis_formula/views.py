from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import BasesCambio, RasPsi


# Create your views here.
class BasesCambioListView(ListView):
    model = BasesCambio
    template_name = 'analisis_formula/bases_cambio_list.html'


class BasesCambioDetailView(DetailView):
    model = BasesCambio
    template_name = 'analisis_formula/bases_cambio_detail.html'
    

class RasPsiListView(ListView):
    model = RasPsi
    template_name = 'analisis_formula/ras_psi_list.html'


class RasPsioDetailView(DetailView):
    model = RasPsi
    template_name = 'analisis_formula/ras_psi_detail.html'
    