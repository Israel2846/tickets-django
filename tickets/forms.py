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
        empty_label="Seleccione una categoría",
        widget=forms.Select(attrs={'class': 'tu-clase-css-aqui'})
    )


class PrioridadForm(forms.ModelForm):
    class Meta:
        model = Prioridad
        fields = ['nombre_prioridad']


class TicketForm(forms.ModelForm):
    categoría = forms.ModelChoiceField(
        queryset=Categoría.objects.all(),
    )
    
    subcategoría = forms.ModelChoiceField(
        queryset=SubCategoría.objects.none(),
    )
    class Meta:
        model = Ticket
        fields = ['id_prioridad', 'documentos_adicionales', 'descripción']