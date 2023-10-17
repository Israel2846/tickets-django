from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_sesion, name='Login'),
    path('cerrar_sesion', views.cerrar_sesion, name='Cerrar sesión'),
    path('index', views.index, name='Inicio'),
    path('crear_usuario', views.usuario, name='Crear usuario'),
    path('categoría', views.categoría, name='Categoría'),
    path('prioridad', views.prioridad, name='Prioridad'),
    path('subcategoría', views.subcategoría, name='Subcategoría'),
    path('cargar_subcategorias', views.cargar_subcategorías, name='Cargar subcategoría'),
    path('crear_ticket', views.ticket, name='Crear ticket'),
    path('consultar_tickets', views.consultar_tickets, name='Consultar tickets'),
    path('detalle_ticket/<int:id>', views.ticket, name='Detalle ticket'),
]