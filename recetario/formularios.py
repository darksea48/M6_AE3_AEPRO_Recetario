from django import forms
import datetime

class FormularioDeEvento(forms.Form):
    evento= forms.CharField(label="Nombre del evento", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    fecha = forms.DateField(initial=datetime.date.today)
    ubicacion = forms.CharField(label="Ubicacion", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))