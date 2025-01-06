from django.contrib import admin
from django.urls import include, path
from control_combustible import views


urlpatterns = [
    path('', views.index, name='index'),
    path('crear_vale/', views.valeCombustible, name='crear_vale'),
]
