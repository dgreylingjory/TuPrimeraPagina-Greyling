from django.contrib import admin
from django.urls import include, path
from inventario import views

app_name = 'inv'

urlpatterns = [
    path('', views.index, name='index'),
]
