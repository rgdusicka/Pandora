from django import forms

class createnewtask(forms.Form):
    title = forms.CharField(label="Titulo", max_length=200, widget=forms.TextInput(attrs={'class': 'form-group-default'}))
    description = forms.CharField(label="Descripcion", widget=forms.Textarea(attrs={'class': 'form-group-default'}))
    Project = forms.ChoiceField(choices =[('1','Noticias'),('2','Nosotros'),('3','Info!')], label='Categoria', widget=forms.Select(attrs={'class': 'form-control'}))

class createnewprojects(forms.Form):
    name = forms.CharField(label="Nombre del Tema", max_length=200, widget=forms.TextInput(attrs={'class': 'form-group-default'}))