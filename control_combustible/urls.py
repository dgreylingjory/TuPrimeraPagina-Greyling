from django.contrib import admin
from django.urls import include, path
from control_combustible import views

app_name = 'cc'

urlpatterns = [
    path('', views.index, name='index'), ##pagina inicio app
    path('crearvale/', views.vale_combustible, name='crear_vale'), ##formulario para crear vale
    path('vervales/', views.ver_vales, name='ver_vales'), ##ver vales
    path('creardatos/', views.crear_clases_home, name='crear_datos'), ##crear datos
    path('creardatos/crearusuario/', views.crear_usuario, name='crear_usuario'), ##crear usuario
    path('creardatos/crearaeronave/', views.crear_aeronave, name='crear_aeronave'), ##crear aeronave
    path('creardatos/crearcamion/', views.crear_camion, name='crear_camion'), ##crear camion
    path('creardatos/crearmodelo/', views.crear_modelo, name='crear_modelo'), ##crear modelo
]