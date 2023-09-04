from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('categoría', views.categoría, name='Categoría'),
    path('categoría/editar-eliminar/<int:id>', views.editar_eliminar_categoría, name='Editar/Eliminar categoría'),
]