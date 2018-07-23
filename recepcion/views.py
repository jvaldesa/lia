from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Recepcion
from generales.models import Municipio
from .forms import RecepcionForm

# Create your views here.

class RecepcionListView(ListView):
    model = Recepcion
    paginate_by = 10


class RecepcionCreateView(CreateView):
    model = Recepcion
    form_class = RecepcionForm
    success_url = reverse_lazy('recepcion:list')


class RecepcionUpdateView(UpdateView):
    model = Recepcion
    form_class = RecepcionForm
    success_url = reverse_lazy('recepcion:list')
    template_name_suffix = '_update_form'

class RecepcionDeleteView(DeleteView):
    model = Recepcion
    success_url = reverse_lazy('recepcion:list')

