from django import forms

class ConsulataForm(forms.Form):
    clave_consulta = forms.CharField(label='Clave de Consulta', max_length=10, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Clave de Consulta'}))
