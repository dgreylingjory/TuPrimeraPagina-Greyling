from django import forms

class Vale_combustible(forms.Form):
    fecha = forms.TimeField(label='Fecha', max_length=100)
    litros_cargados = forms.IntegerField(label='Litros cargados', max_length=6)
    matricula_aeronave = forms.CharField(label='Message', widget=forms.Textarea)
    patente_camion = forms.CharField(label='Patente camión', max_length=6)
    motivo =forms.CharField(label='Motivo', max_length=100)
    despachador = forms.CharField(label='Despachador', max_length=100)
    receptor = forms.CharField(label='Receptor', max_length=100)