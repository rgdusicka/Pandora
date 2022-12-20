from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class createnewtask(forms.Form):
    title = forms.CharField(label="Titulo", max_length=200, widget=forms.TextInput(attrs={'class': 'form-group-default'}))
    description = forms.CharField(label="Descripcion", widget=forms.Textarea(attrs={'class': 'form-group-default'}))
    Project = forms.ChoiceField(choices =[('1','Noticias'),('2','Nosotros'),('3','Info!')], label='Categoria', widget=forms.Select(attrs={'class': 'form-control-sm'}))

class createnewprojects(forms.Form):
    name = forms.CharField(label="Nombre del Tema", max_length=200, widget=forms.TextInput(attrs={'class': 'form-group-default'}))


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

        
class ResgistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'email': 'Correo',
        }

class ResetPasswordForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese un username',
        'class': 'form-control',
        'autocomplete': 'off'
    }))
