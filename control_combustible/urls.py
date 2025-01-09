from django.contrib import admin
from django.urls import include, path
from control_combustible import views


urlpatterns = [
    path('', views.index, name='index'), ##pagina inicio app
    path('crearvale/', views.vale_combustible, name='crear_vale'), ##formulario para crear vale
]