from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView
from main import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
]
