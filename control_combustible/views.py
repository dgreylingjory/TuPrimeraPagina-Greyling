from django.shortcuts import render
from .forms import ValeCombustibleForm
from .models import ValeCombustible

def index(request):
    return render(request, 'control_combustible/index.html')

def vale_combustible(request):
    # Create a form instance, it will be used to display the form and process data.
    form = ValeCombustibleForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        # Get cleaned data from the form
        fecha = form.cleaned_data['fecha']
        litros_cargados = form.cleaned_data['litros_cargados']
        matricula_aeronave = form.cleaned_data['matricula_aeronave']
        patente_camion = form.cleaned_data['patente_camion']
        motivo = form.cleaned_data['motivo']
        despachador = form.cleaned_data['despachador']
        receptor = form.cleaned_data['receptor']

        # Calculate the next ValeCombustible number
        contar_vales = ValeCombustible.objects.count()
        numero_vale = contar_vales + 1

        # Create and save the ValeCombustible instance
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

        # Return a response
        return render(request, 'control_combustible/vale_combustible_respuesta.html', {
            'form': form,
            'mensaje': 'Vale guardado correctamente'
        })
    
    return render(request, 'control_combustible/vale_combustible.html', {'form': form})