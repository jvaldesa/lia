from django import forms
from .models import Recepcion 
from generales.models import Municipio
from django.forms.fields import DateField


select_cultivo = (
    ('', ''),
    ('Maíz', 'Maíz'),
    ('Trigo', 'Trigo'),
    ('Sorgo', 'Sorgo'),
    ('Fresa', 'Fresa'),
    ('Limón', 'Limón'),
    ('Aguacate', 'Aguacate'),
    ('Caña de Azucar', 'Caña de Azucar'),
)

class RecepcionForm(forms.ModelForm):
    class Meta:
        model = Recepcion
        fields = ('folio', 'productor', 'organizacion', 'fecha_recepcion', 'fecha_muestreo', 'tipo_analisis', 'regimen_hidrico', 'estado', 'municipio', 'profundida_cm', 'numero_hectareas', 'cultivo_anterior', 'cultivo_a_establecer', 'rendimiento_esperado', 'estado', 'municipio', 'localidad_ejido' )
        widgets = {
            'folio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Folio'}),
            'productor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Productor'}),
            'organizacion': forms.Select(attrs={'class':'form-control', 'placeholder':'Organización'}),
            'fecha_recepcion': forms.DateInput(attrs={'class':'datepicker form-control', 'placeholder':'Fecha de Recepción'}),
            'fecha_muestreo': forms.DateInput(attrs={'class':'datepicker form-control', 'placeholder':'Fecha de Muestreo'}),
            'tipo_analisis': forms.Select(attrs={'class':'form-control', 'placeholder':'Tipo de Análisis'}),
            'regimen_hidrico': forms.Select(attrs={'class':'form-control', 'placeholder':'Regimen Hidrico'}),
            'profundida_cm': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Profundidad de Muestreo(cm)'}),
            'numero_hectareas': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Número de Hectareas'}),
            'cultivo_anterior': forms.Select(choices=select_cultivo, attrs={'class':'form-control'}),
            'cultivo_a_establecer': forms.Select(choices=select_cultivo, attrs={'class':'form-control'}),
            'rendimiento_esperado': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Rendimiento Esperado(tons)'}),
            'estado': forms.Select(attrs={'class':'form-control', 'placeholder':'Estado'}),
            'municipio': forms.Select(attrs={'class':'form-control', 'placeholder':'Municipio'}),
            'localidad_ejido': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Localidad o Ejido'}),
        }
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['municipio'].queryset = Municipio.objects.none()
        
        if 'estado' in self.data:
            try:
                estado_id = int(self.data.get('estado'))
                self.fields['municipio'].queryset = Municipio.objects.filter(estado_id=estado_id).order_by('nombre')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['municipio'].queryset = self.instance.estado.municipio_set.order_by('nombre')
