from django import forms
from .models import Nitrogeno, CarbonatosTotales, Micronutrientes, BasesIntercambiables, Fosforo
from recepcion.models import Recepcion
from calculos.modelos import filtrarModeloconModelo


#----NITROGENO
class NitrogenoForm(forms.ModelForm):
    class Meta:
        model = Nitrogeno
        fields = [
            'folio',
            'M',
            'B',
            'N',
            'Vi',
            'a',
            'p',
            'analista',
            'fecha_analisis',
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'M': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Titulación (ml)'}),
            'B': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Blanco (ml)'}),
            'N': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Normalidad del Acido'}),
            'Vi': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Volumen Extractante (ml)'}),
            'a': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Alicuota Destilada'}),
            'p': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Peso de la muestra (gr)'}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['folio'].queryset = filtrarModeloconModelo(Recepcion, Nitrogeno).order_by('id')


class NitrogenoFormUpdate(forms.ModelForm):
    class Meta:
        model = Nitrogeno
        fields = [
            'folio',
            'M',
            'B',
            'N',
            'Vi',
            'a',
            'p',
            'analista',
            'fecha_analisis',
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'M': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Titulación (ml)'}),
            'B': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Blanco (ml)'}),
            'N': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Normalidad del Acido'}),
            'Vi': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Volumen Extractante (ml)'}),
            'a': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Alicuota Destilada'}),
            'p': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Peso de la muestra (gr)'}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }



#----CARBONATOS TOTALES
class CarbonatosTotalesForm(forms.ModelForm):
    class Meta:
        model = CarbonatosTotales
        fields = [
            'folio',
            'm',
            'a',
            'b',
            's',
            'analista',
            'fecha_analisis',
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'm': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Molaridad de la solución'}),
            'a': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'ml Titulación Blanco'}),
            'b': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'ml Titulación Muestra'}),
            's': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Peso de la Muestra (gr)'}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['folio'].queryset = filtrarModeloconModelo(Recepcion, CarbonatosTotales).order_by('id')
        

class CarbonatosTotalesFormUpdate(forms.ModelForm):
    class Meta:
        model = CarbonatosTotales
        fields = [
            'folio',
            'm',
            'a',
            'b',
            's',
            'analista',
            'fecha_analisis',
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'm': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Molaridad de la solución'}),
            'a': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'ml Titulación Blanco'}),
            'b': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'ml Titulación Muestra'}),
            's': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Peso de la Muestra (gr)'}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }



#----MICRONUTRIENTES
class MicronutrientesForm(forms.ModelForm):
    class Meta:
        model = Micronutrientes
        fields = [
            'folio',
            'Fe',
            'Cu',
            'Mn',
            'Zn',
            'analista',
            'fecha_analisis',
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'Fe': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Fe'}),
            'Cu': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cu'}),
            'Mn': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Mn'}),
            'Zn': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Zn'}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['folio'].queryset = filtrarModeloconModelo(Recepcion, Micronutrientes).order_by('id')


class MicronutrientesFormUpdate(forms.ModelForm):
    class Meta:
        model = Micronutrientes
        fields = [
            'folio',
            'Fe',
            'Cu',
            'Mn',
            'Zn',
            'analista',
            'fecha_analisis',
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'Fe': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Fe'}),
            'Cu': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cu'}),
            'Mn': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Mn'}),
            'Zn': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Zn'}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }



#----BASES INTERCAMBIABLES
class BasesIntercambiablesForm(forms.ModelForm):
    class Meta:
        model = BasesIntercambiables
        fields = [
            'folio',
            'Ca',
            'Mg',
            'Na',
            'K',
            'analista',
            'fecha_analisis',
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'Ca': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ca'}),
            'Mg': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Mg'}),
            'Na': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Na'}),
            'K': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'K'}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['folio'].queryset = filtrarModeloconModelo(Recepcion, BasesIntercambiables).order_by('id')


class BasesIntercambiablesFormUpdate(forms.ModelForm):
    class Meta:
        model = BasesIntercambiables
        fields = [
            'folio',
            'Ca',
            'Mg',
            'Na',
            'K',
            'analista',
            'fecha_analisis',
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'Ca': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ca'}),
            'Mg': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Mg'}),
            'Na': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Na'}),
            'K': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'K'}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }



#----FOSFORO
tipo_choices = (('', ''), ('P-Bray', 'P-Bray'), ('P-Olsen', 'P-Olsen'))
class FosforoForm(forms.ModelForm):
    class Meta:
        model = Fosforo
        fields = [
            'folio',
            'tipo',
            'fosforo',
            'analista',
            'fecha_analisis',
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'tipo': forms.Select(choices=tipo_choices, attrs={'class':'form-control',}),
            'fosforo': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Fosforo'}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['folio'].queryset = filtrarModeloconModelo(Recepcion, Fosforo).order_by('id')


class FosforoFormUpdate(forms.ModelForm):
    class Meta:
        model = Fosforo
        fields = [
            'folio',
            'tipo',
            'fosforo',
            'analista',
            'fecha_analisis',
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'tipo': forms.Select(choices=tipo_choices, attrs={'class':'form-control',}),
            'fosforo': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Fosforo'}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }


