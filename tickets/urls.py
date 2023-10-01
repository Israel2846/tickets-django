from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Inicio'),
    path('crear_usuario', views.usuario, name='Crear usuario'),
    path('categoría', views.categoría, name='Categoría'),
    path('categoría/editar-eliminar/<int:id>', views.categoría, name='Editar/Eliminar categoría'),
    path('prioridad', views.prioridad, name='Prioridad'),
    path('prioridad/editar-eliminar/<int:id>', views.prioridad, name='Editar/Eliminar prioridad'),
    path('subcategoría', views.subcategoría, name='Subcategoría'),
    path('subcategoría/editar-eliminar/<int:id>', views.subcategoría, name='Editar/Eliminar subcategoría'),
    path('cargar_subcategorias', views.cargar_subcategorías, name='Cargar subcategoría'),
    path('crear_ticket', views.ticket, name='Crear ticket'),
    path('consultar_tickets', views.consultar_tickets, name='Consultar tickets'),
    path('detalle_ticket/<int:id>', views.ticket, name='Detalle ticket'),
]