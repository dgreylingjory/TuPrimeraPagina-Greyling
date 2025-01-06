from django import forms

class ValeCombustibleForm(forms.Form):
    fecha = forms.TimeField(label='Fecha')
    litros_cargados = forms.IntegerField(label='Litros cargados', max_value=999999, min_value=1)
    matricula_aeronave = forms.CharField(label='Matrícula Aeronave', max_length=10)
    patente_camion = forms.CharField(label='Patente camión', max_length=6)
    motivo =forms.CharField(label='Motivo', max_length=100)
    despachador = forms.CharField(label='Despachador', max_length=100)
    receptor = forms.CharField(label='Receptor', max_length=100)