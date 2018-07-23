from django.urls import path
from .views import AnalistaCreateView, AnalistaListView, AnalistaUpdateView, AnalistaDeleteView, CultivoCreateView, CultivoListView, CultivoUpdateView, CultivoDeleteView, EstadoListView, EstadoUpdateView, MunicipioListView, MunicipioUpdateView, OrganizacionCreateView, OrganizacionListView, OrganizacionDetailView, OrganizacionUpdateView, OrganizacionDeleteView, RegimenHidricoCreateView, RegimenHidricoListView, RegimenHidricoUpdateView, RegimenHidricoDeleteView, TipoAnalisisCreateView, TipoAnalisisUpdateView, TipoAnalisisListView, TipoAnalisisDeleteView

from . import views


generales_patterns = ([
    path('analista_create/', AnalistaCreateView.as_view(), name='analista_create'),
    path('analista_list/', AnalistaListView.as_view(), name='analista_list'),
    path('analista_update/<int:pk>', AnalistaUpdateView.as_view() , name='analista_update'),
    path('analista_delete/<int:pk>', AnalistaDeleteView.as_view() , name='analista_delete'),
    #CULTIVO
    path('cultivo_create/', CultivoCreateView.as_view(), name='cultivo_create'),
    path('cultivo_list/', CultivoListView.as_view(), name='cultivo_list'),
    path('cultivo_update/<int:pk>', CultivoUpdateView.as_view() , name='cultivo_update'),
    path('cultivo_delete/<int:pk>', CultivoDeleteView.as_view() , name='cultivo_delete'),
    #ESTADO
    path('estado_list/', EstadoListView.as_view(), name='estado_list'),
    path('estado_update/<int:pk>', EstadoUpdateView.as_view() , name='estado_update'),
     #MUNICIPIO
    path('municipio_list/', MunicipioListView.as_view(), name='municipio_list'),
    path('municipio_update/<int:pk>', MunicipioUpdateView.as_view() , name='municipio_update'),
    #ORGANIZACION
    path('organizacion_create/', OrganizacionCreateView.as_view(), name='organizacion_create'),
    path('organizacion_list/', OrganizacionListView.as_view(), name='organizacion_list'),
    path('organizacion_detail/<int:pk>', OrganizacionDetailView.as_view() , name='organizacion_detail'),
    path('organizacion_update/<int:pk>', OrganizacionUpdateView.as_view() , name='organizacion_update'),
    path('organizacion_delete/<int:pk>', OrganizacionDeleteView.as_view() , name='organizacion_delete'),
    path('ajax/load-municipios/', views.load_municipios, name='ajax_load_municipios'),
    #REGIMEN HIDRICO
    path('regimen_hidrico_create/', RegimenHidricoCreateView.as_view(), name='regimen_hidrico_create'),
    path('regimen_hidrico_list/', RegimenHidricoListView.as_view(), name='regimen_hidrico_list'),
    path('regimen_hidrico_update/<int:pk>', RegimenHidricoUpdateView.as_view() , name='regimen_hidrico_update'),
    path('regimen_hidrico_delete/<int:pk>', RegimenHidricoDeleteView.as_view() , name='regimen_hidrico_delete'),
    #TIPO ANALISIS
    path('tipo_analisis_create/', TipoAnalisisCreateView.as_view(), name='tipo_analisis_create'),
    path('tipo_analisis_list/', TipoAnalisisListView.as_view(), name='tipo_analisis_list'),
    path('tipo_analisis_update/<int:pk>', TipoAnalisisUpdateView.as_view() , name='tipo_analisis_update'),
    path('tipo_analisis_delete/<int:pk>', TipoAnalisisDeleteView.as_view() , name='tipo_analisis_delete'),
], 'generales')