from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_isaac.urls')), # Ruta raíz conectada a home_isaac
]