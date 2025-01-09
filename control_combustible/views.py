from django.shortcuts import render
from .forms import *
from .models import ValeCombustible
##=============================== PAGINA PRINCIPAL ===================================
def index(request):
    return render(request, 'control_combustible/index.html')

##=============================== FORMULARIO CREAR VALE (Crud)========================
def vale_combustible(request):
    ##crea una instancia del form
    form = ValeCombustibleForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        ##recibe la data del form
        fecha = form.cleaned_data['fecha']
        litros_cargados = form.cleaned_data['litros_cargados']
        matricula_aeronave = form.cleaned_data['matricula_aeronave']
        patente_camion = form.cleaned_data['patente_camion']
        motivo = form.cleaned_data['motivo']
        despachador = form.cleaned_data['despachador']
        receptor = form.cleaned_data['receptor']

        ##calcula numero de vale
        contar_vales = ValeCombustible.objects.count()
        numero_vale = contar_vales + 1

        ##guarda la instancia de vale
        vale = ValeCombustible(
            numero_vale=numero_vale,
            fecha=fecha,
            litros_cargados=litros_cargados,
            matricula_aeronave=matricula_aeronave,
            patente_camion=patente_camion,
            motivo=motivo,
            despachador=despachador,
            receptor=receptor
        )
        vale.save()

        ##genera respuesta
        return render(request, 'control_combustible/vale_combustible_respuesta.html', {
            'form': form,
            'mensaje': 'Vale guardado correctamente'
        })
    
    return render(request, 'control_combustible/vale_combustible.html', {'form': form})

##=============================== VER VALES (cRud)====================================
def ver_vales(request):
    if request.method == 'GET':
        form = ValeCombustibleVerForm(request.GET)
        if form.is_valid():
            numero_vale = form.cleaned_data['numero_vale']
            resultado = ValeCombustible.objects.filter(
                numero_vale=numero_vale
            )
            return render(
                request, 
                'control_combustible/vale_combustible_ver_resultado.html', 
                {'resultado' : resultado, 'form': form})
    else:
        form = ValeCombustibleVerForm()
    return render(request, 'control_combustible/vale_combustible_ver.html', {'form': form})
