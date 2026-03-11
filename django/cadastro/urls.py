from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina1),  # página inicial
    path('pagina1/', views.pagina1, name='pagina1'), 
    path('pagina2/', views.pagina2), 
    path('pagina3/', views.pagina3), 
    path('pagina4/', views.pagina4), 
]