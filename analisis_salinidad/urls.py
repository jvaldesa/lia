from django.urls import path
from . import views
from .views import (
    PhCePastaCreateView, PhCePastaDetailView, PhCePastaUpdateView, PhCePastaListView, PhCePastaDeleteView,
    cationesCreate, CationesDetailView, cationesUpdate, CationesListView, CationesDeleteView,
    anionesCreate, AnionesDetailView, anionesUpdate, AnionesListView, AnionesDeleteView,
)

analisis_salinidad_patterns = ([
    #Ph Y CONDUCTIVIDAD ELECTRICA PASTA DE SATURACION
    path('phCePasta_create/', PhCePastaCreateView.as_view(), name='phCePasta_create'),
    path('phCePasta_detail/<int:pk>', PhCePastaDetailView.as_view() , name='phCePasta_detail'),
    path('phCePasta_update/<int:pk>', PhCePastaUpdateView.as_view(), name='phCePasta_update'),
    path('phCePasta_list/', PhCePastaListView.as_view() , name='phCePasta_list'),
    path('phCePasta_delete/<int:pk>', PhCePastaDeleteView.as_view(), name='phCePasta_delete'),
    #CATIONES
    path('cationes_create/', cationesCreate, name='cationes_create'),
    path('cationes_detail/<int:pk>', CationesDetailView.as_view() , name='cationes_detail'),
    path('cationes_update/<int:pk>', cationesUpdate, name='cationes_update'),
    path('cationes_list/', CationesListView.as_view() , name='cationes_list'),
    path('cationes_delete/<int:pk>', CationesDeleteView.as_view(), name='cationes_delete'),
    #ANIONES
    path('aniones_create/', anionesCreate, name='aniones_create'),
    path('aniones_detail/<int:pk>', AnionesDetailView.as_view() , name='aniones_detail'),
    path('aniones_update/<int:pk>', anionesUpdate, name='aniones_update'),
    path('aniones_list/', AnionesListView.as_view() , name='aniones_list'),
    path('aniones_delete/<int:pk>', AnionesDeleteView.as_view(), name='aniones_delete'),

], 'analisis_salinidad')