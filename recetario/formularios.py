from django import forms
import datetime

class FormularioDeEvento(forms.Form):
    evento= forms.CharField(label="Nombre del evento", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
    fecha = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}), required=True)
    ubicacion = forms.CharField(label="Ubicación", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}), required=True)