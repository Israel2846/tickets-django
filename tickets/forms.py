from django import forms
from .models import *


class CategoríaForm(forms.ModelForm):
    class Meta:
        model = Categoría
        fields = ['nombre_cat']


class SubCategoríaForm(forms.ModelForm):
    class Meta:
        model = SubCategoría
        fields = ['id_categoría', 'nombre_subCat']
    id_categoría = forms.ModelChoiceField(
        queryset=Categoría.objects.all(),
        widget=forms.Select(attrs={'class': 'ui dropdown'})
    )


class PrioridadForm(forms.ModelForm):
    class Meta:
        model = Prioridad
        fields = ['nombre_prioridad']


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['id_prioridad', 'documentos_adicionales', 'descripción', 'id_categoría', 'id_subcategoría']