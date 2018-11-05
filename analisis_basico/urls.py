from django.urls import path
from . import views
from .views import (
    TexturaDetailView, TexturaListView, TexturaDeleteView,
    PhCeDetailView, PhCeListView, PhCeDeleteView,
    MateriaOrganicaDetailView, MateriaOrganicaListView, MateriaOrganicaDeleteView,
    ColorDensidadAparenteDetailView, ColorDensidadAparenteListView, ColorDensidadAparenteDeleteView,
    PuntoSaturacionDetailView, PuntoSaturacionListView, PuntoSaturacionDeleteView,
)

analisis_basico_patterns = ([
    #TEXTURA
    path('textura_create/', views.texturaCreate, name='textura_create'),
    path('textura_detail/<int:pk>', TexturaDetailView.as_view() , name='textura_detail'),
    path('textura_update/<int:pk>', views.texturaUpdate, name='textura_update'),
    path('textura_list/', TexturaListView.as_view() , name='textura_list'),
    path('textura_delete/<int:pk>', TexturaDeleteView.as_view(), name='textura_delete'),
    #PH Y CONDUCTIVIDAD ELECTRICA
    path('ph_ce_create/', views.PhCeCreate, name='ph_ce_create'),
    path('ph_ce_detail/<int:pk>', PhCeDetailView.as_view() , name='ph_ce_detail'),
    path('ph_ce_update/<int:pk>', views.PhCeUpdate, name='ph_ce_update'),
    path('ph_ce_list/', PhCeListView.as_view() , name='ph_ce_list'),
    path('ph_ce_delete/<int:pk>', PhCeDeleteView.as_view(), name='ph_ce_delete'),
    #MATERIA ORGANICA
    path('materia_organica_create/', views.materiaOrganicaCreate, name='materia_organica_create'),
    path('materia_organica_detail/<int:pk>', MateriaOrganicaDetailView.as_view() , name='materia_organica_detail'),
    path('materia_organica_update/<int:pk>', views.materiaOrganicaUpdate, name='materia_organica_update'),
    path('materia_organica_list/', MateriaOrganicaListView.as_view() , name='materia_organica_list'),
    path('materia_organica_delete/<int:pk>', MateriaOrganicaDeleteView.as_view(), name='materia_organica_delete'),
    #DENSIDAD APARENTE
    path('color_densidad_aparente_create/', views.colorDensidadAparenteCreate, name='color_densidad_aparente_create'),
    path('color_densidad_aparente_detail/<int:pk>', ColorDensidadAparenteDetailView.as_view() , name='color_densidad_aparente_detail'),
    path('color_densidad_aparente_update/<int:pk>', views.colorDensidadAparenteUpdate, name='color_densidad_aparente_update'),
    path('color_densidad_aparente_list/', ColorDensidadAparenteListView.as_view() , name='color_densidad_aparente_list'),
    path('color_densidad_aparente_delete/<int:pk>', ColorDensidadAparenteDeleteView.as_view(), name='color_densidad_aparente_delete'),
    #PUNTO DE SATURACION
    path('punto_saturacion_create/', views.puntoSaturacionCreate, name='punto_saturacion_create'),
    path('punto_saturacion_detail/<int:pk>', PuntoSaturacionDetailView.as_view() , name='punto_saturacion_detail'),
    path('punto_saturacion_update/<int:pk>', views.puntoSaturacionUpdate, name='punto_saturacion_update'),
    path('punto_saturacion_list/', PuntoSaturacionListView.as_view() , name='punto_saturacion_list'),
    path('punto_saturacion_delete/<int:pk>', PuntoSaturacionDeleteView.as_view(), name='punto_saturacion_delete'),

    
    #path('consulta/', views.consulta, name='consulta'),
    #path('delete/<int:pk>', PageDeleteView.as_view() , name='delete'),
], 'analisis_basico')