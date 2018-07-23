from django.urls import path
from .views import RecepcionListView, RecepcionCreateView, RecepcionUpdateView, RecepcionDeleteView
from . import views

recepcion_patterns = ([
    path('', RecepcionListView.as_view(), name='list'),
    #path('<int:pk>/<slug:page_slug>/', PageDetailView.as_view() , name='page'),
    path('create/', RecepcionCreateView.as_view(), name='create'),
    path('update/<int:pk>', RecepcionUpdateView.as_view() , name='update'),
    path('delete/<int:pk>', RecepcionDeleteView.as_view() , name='delete'),
], 'recepcion')