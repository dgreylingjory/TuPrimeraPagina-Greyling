from django.shortcuts import render
from .forms import *
from .models import ValeCombustible
##=============================== PAGINA PRINCIPAL ===================================
def index(request): ##autoexplicativo
    return render(request, 'control_combustible/index.html')

##=============================== FORMULARIO CREAR VALE (Crud)========================
def vale_combustible(request): ##usa metodo POST para guardar vale en bbdd
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
        numero_vale = form.cleaned_data.get('numero_vale', ValeCombustible.objects.count() + 1)

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
            'mensaje': f'Vale guardado correctamente con número {numero_vale}',
        })
    
    return render(request, 'control_combustible/vale_combustible.html', {'form': form})

##=============================== VER VALES (cRud)====================================
def ver_vales(request): ##usa metodo GET para buscar vale la bbdd
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

##=============================== CREAR DATOS ======================================
def crear_clases_home(request): ##view inicio para creación de clases
    return render(request, 'control_combustible/crear_clases_home.html')

def crear_modelo(request): ##view unica con metodo POST
    if request.method == 'POST': ##misma filosofia que vale_combustible
        form = ModeloForm(request.POST)
        if form.is_valid():
            nombre_modelo = form.cleaned_data['nombre_modelo']
            capacidad_modelo = form.cleaned_data['capacidad_modelo']
            
            modelo = ModeloHelicoptero(
                nombre_modelo=nombre_modelo,
                capacidad_modelo=capacidad_modelo
            )
            modelo.save()

            return render(request, 'control_combustible/crear_clase_respuesta.html', {
                'form': form,
                'mensaje': 'Modelo guardado correctamente',
                'modelo': modelo, ##devuelve el modelo creado para que la pagina respuesta use metodo de clase 
            })

    else:
        form = ModeloForm()
       
    return render(request, 'control_combustible/crear_clase.html', {'form': form})
##views que siguen usan misma filosofia que crear_modelo

def crear_aeronave(request):
    if request.method == 'POST':
        form = AeronaveForm(request.POST)
        if form.is_valid():
            modelo = form.cleaned_data['modelo']
            capacidad = form.cleaned_data['capacidad']
            matricula = form.cleaned_data['matricula']
            
            aeronave = Aeronave(
                modelo=modelo,
                capacidad=capacidad,
                matricula=matricula
            )
            aeronave.save()

            return render(request, 'control_combustible/crear_clase_respuesta.html', {
                'form': form,
                'mensaje': 'Aeronave guardada correctamente',
                'aeronave': aeronave  
            })

        else:
            return render(request, 'control_combustible/crear_clase.html', {'form': form})

    else:
        form = AeronaveForm()

    return render(request, 'control_combustible/crear_clase.html', {'form': form})

def crear_camion(request):
    if request.method == 'POST':
        form = CamionForm(request.POST)
        if form.is_valid():
            patente = form.cleaned_data['patente']
            capacidad = form.cleaned_data['capacidad']
            contenido = form.cleaned_data['contenido']
            vencimiento_filtro = form.cleaned_data['vencimiento_filtro']
            vencimiento_certificacion = form.cleaned_data['vencimiento_certificacion']
            
            camion = Camion(
                patente=patente,
                capacidad=capacidad,
                contenido=contenido,
                vencimiento_filtro=vencimiento_filtro,
                vencimiento_certificacion=vencimiento_certificacion
            )
            camion.save()

            return render(request, 'control_combustible/crear_clase_respuesta.html', {
                'form': form,
                'mensaje': 'Camión guardado correctamente',
                'camion': camion  
            })

        else:
            return render(request, 'control_combustible/crear_clase.html', {'form': form})

    else:
        form = CamionForm()

    return render(request, 'control_combustible/crear_clase.html', {'form': form})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            
            usuario = Usuario(
                nombre=nombre,
                apellido=apellido,
                email=email
            )
            usuario.save()

            return render(request, 'control_combustible/crear_clase_respuesta.html', {
                'form': form,
                'mensaje': 'Usuario guardado correctamente',
                'usuario': usuario  
            })
        else:
            return render(request, 'control_combustible/crear_clase.html', {'form': form})

    else:
        form = UsuarioForm()

    return render(request, 'control_combustible/crear_clase.html', {'form': form})