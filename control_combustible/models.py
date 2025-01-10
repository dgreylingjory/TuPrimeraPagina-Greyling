from django.db import models

# Create your models here.

##============================ MODELOS USADOS EN APP DE COMBUSTIBLE ==============================
class ModeloHelicoptero(models.Model):
    nombre_modelo = models.CharField(max_length = 10)
    capacidad_modelo = models.IntegerField()
    def __str__(self):
        return self.nombre_modelo
    def describir(self):
        return f"Modelo: {self.nombre_modelo}\nCapacidad: {self.capacidad_modelo}"
    
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
    def describir(self):
        return f"Matrícula: {self.matricula}\nModelo: {self.modelo}\nCapacidad: {self.capacidad}"

class Camion(models.Model):
    patente = models.CharField(max_length=6)
    capacidad = models.IntegerField()
    contenido = models.IntegerField()
    vencimiento_filtro = models.DateField()
    vencimiento_certificacion = models.DateField()
    def __str__(self):
        return self.patente
    def describir(self):
        return f"Patente: {self.patente}\nCapacidad: {self.capacidad}\nContenido: {self.contenido}\nVencimiento Filtro: {self.vencimiento_filtro}\nVencimiento Certificación: {self.vencimiento_certificacion}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    def describir(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEmail: {self.email}"

##============================ MODELO PARA FORMULARIO DE VALE ===================================    
class ValeCombustible(models.Model): ##transforma la entrada del form a un objeto
    numero_vale = models.IntegerField(default=0)
    fecha = models.DateField()
    litros_cargados = models.IntegerField()
    matricula_aeronave = models.ForeignKey(Aeronave, on_delete=models.CASCADE)
    patente_camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=100)
    despachador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='despachador')
    receptor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='receptor')
    
    def __str__(self):
        return f"Vale {self.numero_vale} - {self.fecha}"
    
