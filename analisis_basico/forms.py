from django import forms
from .models import Textura, Ph_ConductividadElectrica, MateriaOrganica, ColorDensidadAparente, PuntoSaturacion, Folios
from recepcion.models import Recepcion
from calculos.modelos import filtrarModeloconModelo



#----TEXTURA
class TexturaForm(forms.ModelForm):
    class Meta:
        model = Textura
        fields = ['folio', 'lectura_1', 'lectura_2', 'lectura_3', 'lectura_4', 'temperatura_1', 'temperatura_2', 'temperatura_3', 'temperatura_4', 'arenas', 'arcillas', 'limos', 'textura', 'analista', 'fecha_analisis']
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'lectura_1': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Lectura 1'}), 
            'lectura_2': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Lectura 2'}), 
            'lectura_3': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Lectura 3'}), 
            'lectura_4': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Lectura 4'}), 
            'temperatura_1': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Temperatura 1'}), 
            'temperatura_2': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Temperatura 2'}), 
            'temperatura_3': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Temperatura 3'}), 
            'temperatura_4': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Temperatura 4'}), 
            'arenas': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Arenas'}), 
            'arcillas': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Arcillas'}), 
            'limos': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Limos'}), 
            'textura': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Textura'}), 
            'analista': forms.Select(attrs={'class':'form-control',}), 
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Anális'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['folio'].queryset = filtrarModeloconModelo(Recepcion, Textura).order_by('id')
    

class TexturaFormUpdate(forms.ModelForm):
    class Meta:
        model = Textura
        fields = ['folio', 'lectura_1', 'lectura_2', 'lectura_3', 'lectura_4', 'temperatura_1', 'temperatura_2', 'temperatura_3', 'temperatura_4', 'analista', 'fecha_analisis']
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'lectura_1': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Lectura 1'}), 
            'lectura_2': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Lectura 2'}), 
            'lectura_3': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Lectura 3'}), 
            'lectura_4': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Lectura 4'}), 
            'temperatura_1': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Temperatura 1'}), 
            'temperatura_2': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Temperatura 2'}), 
            'temperatura_3': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Temperatura 3'}), 
            'temperatura_4': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Temperatura 4'}), 
            'analista': forms.Select(attrs={'class':'form-control',}), 
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Anális'}),
        }



#-----PH Y CONDUCTIVIDAD ELECTRICA

unidad_choices = (('', ''), ('µS/cm', 'µS/cm'), ('mS/cm', 'mS/cm'))

class PhyCeForm(forms.ModelForm):
    class Meta:
        model = Ph_ConductividadElectrica
        fields = ['folio', 'ph', 'ce', 'unidad', 'analista', 'fecha_analisis']
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
        self.fields['folio'].queryset = filtrarModeloconModelo(Recepcion, Ph_ConductividadElectrica).order_by('id')


class PhyCeFormUpdate(forms.ModelForm):
    class Meta:
        model = Ph_ConductividadElectrica
        fields = ['folio', 'ph', 'ce', 'unidad', 'analista', 'fecha_analisis']
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'ph': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'ph'}),
            'ce': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Conductividad Eléctrica'}),
            'unidad': forms.Select(choices=unidad_choices, attrs={'class':'form-control',}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
         }



#-----MATERIA ORGANICA
clase_suelo_choices = (('', ''), ('Suelos volcánicos', 'Suelos volcánicos'), ('Suelos no volcánicos', 'Suelos no volcánicos'))

class MateriaOrganicaForm(forms.ModelForm):
    class Meta:
        model = MateriaOrganica
        fields = [
            'folio',
            'clase_suelo',
            'b1',
            'b2',
            'b3',
            't',
            'g',
            'N',
            'analista',
            'fecha_analisis', 
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'clase_suelo': forms.Select(choices=clase_suelo_choices, attrs={'class':'form-control',}),
            'b1': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'B1 (ml)'}),
            'b2': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'B2 (ml)'}),
            'b3': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'B3 (ml)'}),
            't': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'T (ml)'}),
            'g': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'g (gr)'}),
            'N': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'N'}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['folio'].queryset = filtrarModeloconModelo(Recepcion, MateriaOrganica). order_by('id')


class MateriaOrganicaFormUpdate(forms.ModelForm):
    class Meta:
        model = MateriaOrganica
        fields = [
            'folio',
            'clase_suelo',
            'b1',
            'b2',
            'b3',
            't',
            'g',
            'N',
            'analista',
            'fecha_analisis', 
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'clase_suelo': forms.Select(choices=clase_suelo_choices, attrs={'class':'form-control',}),
            'b1': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'B1 (ml)'}),
            'b2': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'B2 (ml)'}),
            'b3': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'B3 (ml)'}),
            't': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'T (ml)'}),
            'g': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'g (gr)'}),
            'N': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'N'}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }



#-----COLOR Y DENSIDAD APARENTE
class ColorDensidadAparenteForm(forms.ModelForm):
    class Meta:
        model = ColorDensidadAparente
        fields = [
            'folio',
            'clave',
            'color',
            'peso',
            'volumen',
            'analista',
            'fecha_analisis', 
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'clave': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Clave'}),
            'color': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Color'}),
            'peso': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Peso (gr)'}),
            'volumen': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Volumen (ml)'}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['folio'].queryset = filtrarModeloconModelo(Recepcion, ColorDensidadAparente).order_by('id')


class ColorDensidadAparenteFormUpdate(forms.ModelForm):
    class Meta:
        model = ColorDensidadAparente
        fields = [
            'folio',
            'clave',
            'color',
            'peso',
            'volumen',
            'analista',
            'fecha_analisis', 
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'clave': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Clave'}),
            'color': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Color'}),
            'peso': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Peso (gr)'}),
            'volumen': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Volumen (ml)'}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }  


#-----PUNTO DE SATURACION
class PuntoSaturacionForm(forms.ModelForm):
    class Meta:
        model = PuntoSaturacion
        fields = [
            'folio',
            'peso_inicial_estufa',
            'peso_final_estufa',
            'agua_gastada_estufa',
            'peso_inicial_aire',
            'peso_final_aire',
            'agua_gastada_aire',
            'analista',
            'fecha_analisis',
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'peso_final_estufa': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Peso Final (gr)'}),
            'agua_gastada_estufa': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Agua Gastada (ml)'}),
            'peso_inicial_aire': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Peso Inicial (gr)'}),
            'peso_final_aire': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Peso Final (gr)'}),
            'agua_gastada_aire': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Agua Gastada (ml)'}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['folio'].queryset = filtrarModeloconModelo(Recepcion, PuntoSaturacion). order_by('id')

    def clean_peso_final_estufa(self):
        peso_final_estufa = self.cleaned_data.get('peso_final_estufa')
        if peso_final_estufa <= 0:
            raise forms.ValidationError('Este valor no puede ser 0 o menor a 0')
        return peso_final_estufa

    def clean_peso_final_aire(self):
        peso_final_aire = self.cleaned_data.get('peso_final_aire')
        if peso_final_aire <= 0:
            raise forms.ValidationError('Este valor no puede ser 0 o menor a 0')
        return peso_final_aire
        

class PuntoSaturacionFormUpdate(forms.ModelForm):
    class Meta:
        model = PuntoSaturacion
        fields = [
            'folio',
            'peso_inicial_estufa',
            'peso_final_estufa',
            'agua_gastada_estufa',
            'peso_inicial_aire',
            'peso_final_aire',
            'agua_gastada_aire',
            'analista',
            'fecha_analisis',
        ]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
            'peso_inicial_estufa': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Peso Inicial (gr)'}),
            'peso_final_estufa': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Peso Final (gr)'}),
            'agua_gastada_estufa': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Agua Gastada (ml)'}),
            'peso_inicial_aire': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Peso Inicial (gr)'}),
            'peso_final_aire': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Peso Final (gr)'}),
            'agua_gastada_aire': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Agua Gastada (ml)'}),
            'analista': forms.Select(attrs={'class':'form-control',}),
            'fecha_analisis': forms.DateInput(attrs={'class':'form-control datepicker', 'placeholder':'Fecha de Análisis'}),
        }























# EJERCICIO DE CONSULTA DE RESULTADOS   
class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Folios
        fields = ['folio',]
        widgets = {
            'folio': forms.Select(attrs={'class':'form-control'}),
        }
