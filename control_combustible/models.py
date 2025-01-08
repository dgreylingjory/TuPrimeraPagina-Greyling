from django.db import models

# Create your models here.
class ModeloHelicoptero(models.Model):
    nombre_modelo = models.CharField(max_length = 10)
    capacidad_modelo = models.IntegerField()
    def __str__(self):
        return self.nombre_modelo
class Aeronave(models.Model):
    modelo = models.ForeignKey(
        ModeloHelicoptero,
        on_delete=models.CASCADE,
        related_name='modelo'
        )
    capacidad = models.IntegerField()
    matricula = models.CharField(max_length=6)
    def __str__(self):
        return self.matricula

class Camion(models.Model):
    patente = models.CharField(max_length=6)
    capacidad = models.IntegerField()
    contenido = models.IntegerField()
    vencimiento_filtro = models.DateField()
    vencimiento_certificacion = models.DateField()
    def __str__(self):
        return self.patente

class Despachador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    privilegios = models.CharField(max_length=1)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Receptor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class ValeCombustible(models.Model):
    fecha = models.DateTimeField()
    litros_cargados = models.IntegerField()
    matricula_aeronave = models.CharField(Aeronave, max_length=10)
    patente_camion = models.CharField(Camion, max_length=6)
    motivo = models.CharField(max_length=100)
    despachador = models.CharField(Despachador, max_length=100)
    receptor = models.CharField(Receptor, max_length=100)
    
