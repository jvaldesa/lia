from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.dashboard2, name='dashboard'),
    path('', views.dashboard, name='dashboard_n'),
]