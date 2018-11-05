"""laboratorio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from recepcion.urls import recepcion_patterns
from analisis_basico.urls import analisis_basico_patterns
from analisis_nutrientes.urls import analisis_nutrientes_patterns
from analisis_salinidad.urls import analisis_salinidad_patterns
from analisis_formula.urls import analisis_formula_patterns
from reportes.urls import reportes_patterns
from generales.urls import generales_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    
    path('', include('core.urls')),
    #path('dashboard/', include('dashboard.urls')),
    path('recepcion/', include(recepcion_patterns)),
    path('analisis/', include(analisis_basico_patterns)),
    path('analisis/', include(analisis_nutrientes_patterns)),
    path('analisis/', include(analisis_salinidad_patterns)),
    path('analisis/', include(analisis_formula_patterns)),
    path('reportes/', include(reportes_patterns)),
    path('generales/', include(generales_patterns)),
]
