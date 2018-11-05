from django.urls import path
from .views import reporte_UsuariosPDF, ResultadosTotalListView, Reporte_Staff_PDF


reportes_patterns = ([
    path('reporte_PDF/', reporte_UsuariosPDF.as_view(), name='reporte_PDF'),
    path('reporte/<int:pk>', Reporte_Staff_PDF.as_view(), name='reporte_detail'),
    path('', ResultadosTotalListView.as_view(), name='list'),
], 'reportes')