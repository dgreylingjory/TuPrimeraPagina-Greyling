from django.shortcuts import render
from .forms import ValeCombustibleForm
from .models import ValeCombustible

def index(request):
    return render(request, 'control_combustible/index.html', {})

def valeCombustible(request):
    if request.method == 'POST':
        form = ValeCombustibleForm(request.POST)
        if form.is_valid():
            ##procesa datos del form
            fecha = form.cleaned_data['fecha']
            litros_cargados = form.cleaned_data['litros_cargados']
            matricula_aeronave = form.cleaned_data['matricula_aeronave']
            patente_camion = form.cleaned_data['patente_camion']
            motivo = form.cleaned_data['motivo']
            despachador = form.cleaned_data['despachador']
            receptor = form.cleaned_data['receptor']
            ##guarda datos en bbdd
            vale = ValeCombustible(fecha=fecha, litros_cargados=litros_cargados, matricula_aeronave=matricula_aeronave, patente_camion=patente_camion, motivo=motivo, despachador=despachador, receptor=receptor)
            vale.save()
            return render(request, 'control_combustible/vale_combustible.html')
        
    else:
        form = ValeCombustibleForm()

    return render(request, 'control_combustible/vale_combustible.html', {'form': form})
