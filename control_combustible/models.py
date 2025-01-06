from django.db import models

# Create your models here.
class aeronave(models.Model):
    modelo = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    matricula = models.CharField(max_length=6)

class camion(models.Model):
    patente = models.CharField(max_length=6)
    capacidad = models.IntegerField()
    contenido = models.IntegerField()
    vencimiento_filtro = models.DateField()
    vencimiento_certificacion = models.DateField()

class estanque(models.Model):
    numero_estanque = models.IntegerField()
    capacidad = models.IntegerField()
    contenido = models.IntegerField()
    vencimiento_filtro = models.DateField()
       
class tambor(models.Model):
    capacidad = models.IntegerField()
    contenido = models.IntegerField()

class despachador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    privilegios = models.CharField(max_length=1)

class receptor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
class ValeCombustible(models.Model):
    fecha = models.DateTimeField()
    litros_cargados = models.IntegerField()
    matricula_aeronave = models.ForeignKey(aeronave)
    patente_camion = models.ForeignKey(camion)
    motivo = models.CharField(max_length=100)
    despachador = models.ForeignKey(despachador)
    receptor = models.ForeignKey(receptor)
    estanque = models.ForeignKey(estanque)
    
