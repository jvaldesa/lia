from django import forms
from .models import Analista, Cultivo, Estado, Municipio, Organizacion, RegimenHidrico, TipoAnalisis


class AnalistaForm(forms.ModelForm):
    class Meta:
        model = Analista
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Analista'})
        }


class CultivoForm(forms.ModelForm):
    class Meta:
        model = Cultivo
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Cultivo'})
        }


class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Estado'})
        }


class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ['nombre']
        widgets = {
            # 'estado': forms.Select(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Estado'})
        }


class OrganizacionForm(forms.ModelForm):
    class Meta:
        model = Organizacion
        fields = ['nombre', 'estado', 'municipio', 'localidad', 'calle', 'numero_exterior', 'numero_interior', 'colonia', 'codigo_postal', 'rfc', 'telefono_1', 'telefono_2', 'telefono_3', 'correo_electronico_1', 'correo_electronico_2', 'contacto_1', 'puesto_contacto_1', 'telefono_contacto1', 'correo_electronico_contacto_1', 'contacto_2', 'puesto_contacto_2', 'telefono_contacto_2', 'correo_electronico_contacto_2']
        widgets = {
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}), 
        'estado': forms.Select(attrs={'class':'form-control'}), 
        'municipio': forms.Select(attrs={'class':'form-control'}), 
        'localidad': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Localidad'}), 
        'calle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Calle'}), 
        'numero_exterior': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Número Exterior'}), 
        'numero_interior': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Número Interior'}), 
        'colonia': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Colonia'}), 
        'codigo_postal': forms.NumberInput(attrs={'class':'form-control','placeholder':'Codigo Postal'}),
        'rfc': forms.TextInput(attrs={'class':'form-control', 'placeholder':'RFC'}), 
        'telefono_1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefono 1'}), 
        'telefono_2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefono'}), 
        'telefono_3': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefono'}), 
        'correo_electronico_1': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Correo Eléctronico'}), 
        'correo_electronico_2': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Correo Eléctronico'}), 
        'contacto_1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de Contacto'}), 
        'puesto_contacto_1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Puesto de Contacto'}), 
        'telefono_contacto1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Teléfono de Contacto'}), 
        'correo_electronico_contacto_1': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Correo Eléctronico de Contacto'}), 
        'contacto_2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de Contacto'}), 
        'puesto_contacto_2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Puesto de Contacto'}), 
        'telefono_contacto_2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Teléfono de Contacto'}), 
        'correo_electronico_contacto_2': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Correo Eléctronico de Contacto'})
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



class RegimenHidricoForm(forms.ModelForm):
    class Meta:
        model = RegimenHidrico
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Regimen Hidrico'})
        }


class TipoAnalisisForm(forms.ModelForm):
    class Meta:
        model = TipoAnalisis
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tipo de Anáñisis'})
        }

class SearchForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ['estado']
        widgets = {
            'estado': forms.Select(attrs={'class':'form-control'}),
            
        }