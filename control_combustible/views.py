from django.shortcuts import render
from .forms import ValeCombustibleForm
from .models import ValeCombustible

def index(request):
    return render(request, 'control_combustible/index.html')

def vale_combustible(request):
    form = ValeCombustibleForm(request.POST)
    if request.method == 'POST': 
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
            return render(request, 'control_combustible/vale_combustible.html', {'form': form, 'mensaje': 'Vale guardado correctamente'})
            
        else:
            form = ValeCombustibleForm()
            return render(request, 'control_combustible/vale_combustible.html', {'form': form, 'mensaje': 'Error en el formulario'})
            

    return render(request, 'control_combustible/vale_combustible.html', {'form': form})
