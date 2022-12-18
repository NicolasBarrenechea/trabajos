from django import forms
from .models import Inscritos
from .choices import estados


class Inscritosform(forms.ModelForm):
    nombre=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control mb-3 ',
        'type':'text'
        }),label="Nombre")

    telefono=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control mb-3'
    }),label="Telefono")

    fechaInscripcion=forms.DateField(widget=forms.DateInput(attrs={
        'class':'form-control mb-3',
        'type':'date'
    }),label="Fecha inscripcion")

    horaInscripcion=forms.TimeField(widget=forms.TimeInput(attrs={
        'type':'time',
        'class':'form-control mb-3'
    }),label="Hora inscripcion")

    estado=forms.ChoiceField(choices=estados)

    observacion=forms.CharField(required=False ,widget=forms.TextInput(attrs={
        'class':'form-control',
    }),label="Observacion")


    class Meta:
        model=Inscritos
        fields ='__all__'
