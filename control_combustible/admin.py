from django.contrib import admin
from .models import *

##registra modelos en pagina admin
admin.site.register(Aeronave)
admin.site.register(Camion)
admin.site.register(Usuario)
admin.site.register(ValeCombustible)
admin.site.register(ModeloHelicoptero)