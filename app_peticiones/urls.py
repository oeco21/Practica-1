from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca/', views.acerca_de_mi, name='acerca_de_mi'),
    path('hola/<str:primer_nombre>/', views.hola, name='hola'),
    path('suma/<int:num1>/<int:num2>/', views.calcula_suma, name='calcula_suma'),
]