from django import forms

class createnewtask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description=forms.CharField(label="descripcion de la tarea", widget=forms.Textarea(attrs={'class': 'input'}))

class createnewprojects(forms.Form):
    name = forms.CharField(label="Nombre del Proyect", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))