from django import forms
from .models import PhCePasta, Cationes, Aniones
from recepcion.models import Recepcion
from calculos.modelos import filtrarModeloconModelo



#-----PH Y CONDUCTIVIDAD ELECTRICA EN PASTA DE SATURACIÓN

unidad_choices = (('', ''), ('µS/cm', 'µS/cm'), ('mS/cm', 'mS/cm'))

class PhCePastaForm(forms.ModelForm):
    class Meta:
        model = PhCePasta
        fields = [
            'folio', 
            'ph', 
            'ce', 
            'unidad', 
            'analista', 
            'fecha_analisis'
            ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'ph': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ph'}),
            'ce': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Conductividad Eléctrica'}),
            'unidad': forms.Select(choices=unidad_choices, attrs={'class':'form-control',}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
         }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['folio'].queryset = filtrarModeloconModelo(Recepcion, PhCePasta).order_by('id')


class PhCePastaFormUpdate(forms.ModelForm):
    class Meta:
        model = PhCePasta
        fields = [
            'folio',
            'ph', 
            'ce',
            'unidad',
            'analista',
            'fecha_analisis'
            ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'ph': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'ph'}),
            'ce': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Conductividad Eléctrica'}),
            'unidad': forms.Select(choices=unidad_choices, attrs={'class':'form-control',}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
         }




#-----CATIONES
class CationesForm(forms.ModelForm):
    class Meta:
        model = Cationes
        fields = [
            'folio',
            'titulacionCaMg',
            'normalidadEDTA',
            'titulacionCa',
            'alicuota',
            'Na',
            'K',
            'analista', 
            'fecha_analisis',
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'titulacionCaMg': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Titulación Ca+Mg'}),
            'normalidadEDTA': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Normalidad EDTA'}),
            'titulacionCa': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Titulación Ca'}),
            'alicuota': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Alicuota'}),
            'Na': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Na (ppm)'}),
            'K': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'K (ppm)'}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['folio'].queryset = filtrarModeloconModelo(Recepcion, Cationes).order_by('id')



class CationesFormUpdate(forms.ModelForm):
    class Meta:
        model = Cationes
        fields = [
            'folio',
            'titulacionCaMg',
            'normalidadEDTA',
            'titulacionCa',
            'alicuota',
            'Na',
            'K',
            'analista', 
            'fecha_analisis',
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'titulacionCaMg': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Titulación Ca+Mg'}),
            'normalidadEDTA': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Normalidad EDTA'}),
            'titulacionCa': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Titulación Ca'}),
            'alicuota': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Alicuota'}),
            'Na': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Na (ppm)'}),
            'K': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'K (ppm)'}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }




#-----ANIONES
class AnionesForm(forms.ModelForm):
    class Meta:
        model = Aniones
        fields = [
            'folio',
            'titulacionCar',
            'titulacionBlancoCar',
            'normalidadH2SO4',
            'alicuotaCar',
            'titulacionBic',
            'titulacionBlancoBic',
            'alicuotaBic',
            'titulacionClo',
            'titulacionBlancoClo',
            'normalidadAgNO3',
            'alicuotaClo',
            'conductividadEl',
            'unidad',
            'analista', 
            'fecha_analisis',
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'titulacionCar': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Titulación Carbonatos'}),
            'titulacionBlancoCar': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Titulación Blanco'}),
            'normalidadH2SO4': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Normalidad H2SO4'}),
            'alicuotaCar': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Alicuota'}),
            'titulacionBic': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Titulación Bicarbonatos'}),
            'titulacionBlancoBic': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Titulación Blanco'}),
            'alicuotaBic': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Alicuota'}),
            'titulacionClo': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Titulación Cloruros'}),
            'titulacionBlancoClo': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Titulación Blanco'}),
            'normalidadAgNO3': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Normalidad AgNO3'}),
            'alicuotaClo': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Alicuota'}),
            'conductividadEl': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Coductividad Eléctrica'}),
            'unidad': forms.Select(choices=unidad_choices, attrs={'class':'form-control',}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['folio'].queryset = filtrarModeloconModelo(Recepcion, Cationes).order_by('id')



class AnionesFormUpdate(forms.ModelForm):
    class Meta:
        model = Aniones
        fields = [
            'folio',
            'titulacionCar',
            'titulacionBlancoCar',
            'normalidadH2SO4',
            'alicuotaCar',
            'titulacionBic',
            'titulacionBlancoBic',
            'alicuotaBic',
            'titulacionClo',
            'titulacionBlancoClo',
            'normalidadAgNO3',
            'alicuotaClo',
            'conductividadEl',
            'unidad',
            'analista', 
            'fecha_analisis',
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'titulacionCar': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Titulación Carbonatos'}),
            'titulacionBlancoCar': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Titulación Blanco'}),
            'normalidadH2SO4': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Normalidad H2SO4'}),
            'alicuotaCar': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Alicuota'}),
            'titulacionBic': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Titulación Bicarbonatos'}),
            'titulacionBlancoBic': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Titulación Blanco'}),
            'alicuotaBic': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Alicuota'}),
            'titulacionClo': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Titulación Cloruros'}),
            'titulacionBlancoClo': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Titulación Blanco'}),
            'normalidadAgNO3': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Normalidad AgNO3'}),
            'alicuotaClo': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Alicuota'}),
            'conductividadEl': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Coductividad Eléctrica'}),
            'unidad': forms.Select(choices=unidad_choices, attrs={'class':'form-control',}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }