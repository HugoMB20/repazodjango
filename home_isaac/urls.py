from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('genero/accion/', views.genero_accion, name='genero_accion'),
    path('genero/ciencia-ficcion/', views.genero_scifi, name='genero_scifi'),
]