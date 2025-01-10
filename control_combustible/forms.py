from django import forms
from .models import * 

##============================ FORMULARIO CREACION DE VALE ==============================
class ValeCombustibleForm(forms.Form):
    numero_vale = forms.IntegerField(
        required=False, 
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control w-25'})
        )
    fecha = (forms.DateField(
        label='Fecha', 
        widget=forms.DateInput(attrs={'type': 'date'})) ##permite entrada de fecha por seleccion de un calendario
        ) 
    litros_cargados = forms.IntegerField(
        label='Litros cargados', 
        max_value=999999, ##entrada numerica limitado a cantidades racionales
        min_value=1) 
    matricula_aeronave = forms.ModelChoiceField(
        queryset=Aeronave.objects.all(), ##permite seleccionar de clases aeronave
        label='Matrícula Aeronave', 
        empty_label="Seleccione una aeronave",)
    patente_camion = forms.ModelChoiceField(
        queryset=Camion.objects.all(), ##permite seleccionar de clases camion
        label='Patente camión',
        empty_label="Seleccione un camión",)
    motivo =forms.CharField(
        label='Motivo', 
        max_length=100)
    despachador = forms.ModelChoiceField(
        queryset=Usuario.objects.all(), ##permite seleccionar de clases despachador
        label='Despachador', 
        empty_label="Seleccione un despachador",)
    receptor = forms.ModelChoiceField(
        queryset=Usuario.objects.all(), ##permite seleccionar de clases receptor
        label='Receptor', 
        empty_label="Seleccione un receptor",
        )
    def __init__(self, *args, **kwargs):
        ##inicializa el formulario con el numero de vale
        super().__init__(*args, **kwargs)
        if not kwargs.get('initial'):
            self.fields['numero_vale'].initial = ValeCombustible.objects.count() + 1

##============================ FORMULARIO LECTURA DE VALES ==============================
class ValeCombustibleVerForm(forms.Form):
    numero_vale = forms.IntegerField(
        required=True,
        )

##============================ FORMULARIO CREACION DATOS ================================
class ModeloForm(forms.Form):
    nombre_modelo = forms.CharField(
        required=True,
        label='Modelo de la Aeronave', 
        max_length=10,
        empty_value='Ingrese un modelo')
    capacidad_modelo = forms.IntegerField(
        required=True,
        label='Capacidad de Combustible del Modelo en Litros', 
        max_value=999999, 
        min_value=1)  

class AeronaveForm(forms.Form):
    modelo = forms.ModelChoiceField(
        queryset=ModeloHelicoptero.objects.all(),
        label='Modelo de la Aeronave',
        empty_label="Seleccione un modelo",
        )
    capacidad = forms.IntegerField(
        required=True,
        label='Capacidad de Combustible de la Aeronave en Litros', 
        max_value=999999, 
        min_value=1) 
    matricula = forms.CharField(
        required=True,
        label='Matrícula de la Aeronave', 
        max_length=6,
        empty_value='Ingrese una matrícula')

class CamionForm(forms.Form):
    patente = forms.CharField(
        required=True,
        label='Patente del Camión', 
        max_length=6,
        empty_value='Ingrese una patente')
    capacidad = forms.IntegerField(
        required=True,
        label='Capacidad de Combustible del Camión en Litros', 
        max_value=999999, 
        min_value=1) 
    contenido = forms.IntegerField(
        required=True,
        label='Contenido de Combustible del Camión', 
        max_value=999999, 
        min_value=1) 
    vencimiento_filtro = forms.DateField(
        required=True,
        label='Vencimiento del Filtro del Camión', 
        widget=forms.DateInput(attrs={'type': 'date'}))
    vencimiento_certificacion = forms.DateField(
        required=True,
        label='Vencimiento de la Certificación del Camión', 
        widget=forms.DateInput(attrs={'type': 'date'}))  

class UsuarioForm(forms.Form):
    nombre = forms.CharField(
        required=True,
        label='Nombre del Usuario', 
        max_length=50,
        empty_value='Ingrese nombre')
    apellido = forms.CharField(
        required=True,
        label='Apellido del Usuario', 
        max_length=50,
        empty_value='Ingrese apellido')
    email = forms.EmailField(
        required=True,
        label='Email del Usuario', 
        max_length=50,
        empty_value='Ingrese email')