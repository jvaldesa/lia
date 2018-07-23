from django.urls import path
from . import views
from .views import (
    NitrogenoDetailView, NitrogenoListView, NitrogenoDeleteView,
    CarbonatosDetailView, CarbonatosListView, CarbonatosDeleteView,
    MicronutrientesCreateView, MicronutrientesDetailView, MicronutrientesUpdateView, MicronutrientesListView, MicronutrientesDeleteView,
    BasesIntercambiablesCreateView, BasesIntercambiablesDetailView, BasesIntercambiablesUpdateView, BasesIntercambiablesListView, BasesIntercambiablesDeleteView,
    FosforoCreateView, FosforoDetailView, FosforoUpdateView, FosforoListView, FosforoDeleteView,
)

analisis_nutrientes_patterns = ([
    #NITROGENO
    path('nitrogeno_create/', views.nitrogenoCreate, name='nitrogeno_create'),
    path('nitrogeno_detail/<int:pk>', NitrogenoDetailView.as_view() , name='nitrogeno_detail'),
    path('nitrogeno_update/<int:pk>', views.nitrogenoUpdate, name='nitrogeno_update'),
    path('nitrogeno_list/', NitrogenoListView.as_view() , name='nitrogeno_list'),
    path('nitrogeno_delete/<int:pk>', NitrogenoDeleteView.as_view(), name='nitrogeno_delete'),
    #CARBONATOS TOTALES
    path('carbonatos_create/', views.carbonatosCreate, name='carbonatos_create'),
    path('carbonatos_detail/<int:pk>', CarbonatosDetailView.as_view() , name='carbonatos_detail'),
    path('carbonatos_update/<int:pk>', views.carbonatosUpdate, name='carbonatos_update'),
    path('carbonatos_list/', CarbonatosListView.as_view() , name='carbonatos_list'),
    path('carbonatos_delete/<int:pk>', CarbonatosDeleteView.as_view(), name='carbonatos_delete'),
    #MICRONUTRIENTES
    path('micronutrientes_create/', MicronutrientesCreateView.as_view(), name='micronutrientes_create'),
    path('micronutrientes_detail/<int:pk>', MicronutrientesDetailView.as_view() , name='micronutrientes_detail'),
    path('micronutrientes_update/<int:pk>', MicronutrientesUpdateView.as_view(), name='micronutrientes_update'),
    path('micronutrientes_list/', MicronutrientesListView.as_view() , name='micronutrientes_list'),
    path('micronutrientes_delete/<int:pk>', MicronutrientesDeleteView.as_view(), name='micronutrientes_delete'),
    #BASES INTERCAMBIABLES
    path('bases_intercambiables_create/', BasesIntercambiablesCreateView.as_view(), name='bases_intercambiables_create'),
    path('bases_intercambiables_detail/<int:pk>', BasesIntercambiablesDetailView.as_view() , name='bases_intercambiables_detail'),
    path('bases_intercambiables_update/<int:pk>', BasesIntercambiablesUpdateView.as_view(), name='bases_intercambiables_update'),
    path('bases_intercambiables_list/', BasesIntercambiablesListView.as_view() , name='bases_intercambiables_list'),
    path('bases_intercambiables_delete/<int:pk>', BasesIntercambiablesDeleteView.as_view(), name='bases_intercambiables_delete'),
    #FOSFORO
    path('fosforo_create/', FosforoCreateView.as_view(), name='fosforo_create'),
    path('fosforo_detail/<int:pk>', FosforoDetailView.as_view() , name='fosforo_detail'),
    path('fosforo_update/<int:pk>', FosforoUpdateView.as_view(), name='fosforo_update'),
    path('fosforo_list/', FosforoListView.as_view() , name='fosforo_list'),
    path('fosforo_delete/<int:pk>', FosforoDeleteView.as_view(), name='fosforo_delete'),

], 'analisis_nutrientes')