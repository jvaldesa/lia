from django.urls import path
from .views import BasesCambioListView, BasesCambioDetailView, RasPsiListView, RasPsioDetailView



analisis_formula_patterns = ([
    #BASES DE CAMBIO
    path('bases_cambio_detail/<int:pk>', BasesCambioDetailView.as_view() , name='bases_cambio_detail'),
    path('bases_cambio_list/', BasesCambioListView.as_view() , name='bases_cambio_list'),
    #RAS Y PSI
    path('ras_psi_detail/<int:pk>', RasPsioDetailView.as_view() , name='ras_psi_detail'),
    path('ras_psi_list/', RasPsiListView.as_view() , name='ras_psi_list'),

], 'analisis_formula')