from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationFormEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres como maximo y debe ser valido')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    #Validar que el email no se encuentre ya registrado en la base de datos
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya esta registrado, prueba con otro.')
        return email