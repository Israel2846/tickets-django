from django.shortcuts import render, redirect
from .forms import *
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'base.html')


def categoría(request):
    mensaje = None
    if request.POST:
        try:
            formulario = CategoríaForm(request.POST)
            if formulario.is_valid():
                formulario.save()
        except Exception as e:
            mensaje = str(e)
    categorías = Categoría.objects.all()
    return render(request, 'categoría/index.html', {'formulario' : CategoríaForm, 'mensaje' : mensaje,'categorías' : categorías,})


def editar_eliminar(request, id):
    mensaje = None
    categoría = Categoría.objects.get(pk = id)
    formulario = CategoríaForm(instance=categoría)
    if request.POST:
        try:
            accion = request.POST.get('acciones')
            if accion == 'editar':            
                formulario = CategoríaForm(request.POST, instance=categoría)
                if formulario.is_valid():
                    formulario.save()
            elif accion == 'eliminar':
                categoría.delete()
            return redirect('Categoría')
        except Exception as e:
            mensaje = str(e)
    return render(request, 'categoría/editar-eliminar.html', {'mensaje' : mensaje,'formulario' : formulario,})