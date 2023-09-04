from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('categoría', views.categoría, name='Categoría'),
    path('categoría/editar-eliminar/<int:id>', views.editar_eliminar_categoría, name='Editar/Eliminar categoría'),
    path('prioridad', views.prioridad, name='Prioridad'),
    path('prioridad/editar-eliminar/<int:id>', views.editar_eliminar_prioridad, name='Editar/Eliminar prioridad'),
    path('subcategoría', views.subcategoría, name='Subcategoría'),
    path('cargar_subcategorias', views.cargar_subcategorías, name='Cargar subcategoría'),
    path('crear_ticket', views.crear_ticket, name='Crear ticket'),
]