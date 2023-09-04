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


def editar_eliminar_categoría(request, id):
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


def subcategoría(request):
    mensaje = None
    if request.POST:
        try:
            formulario = SubCategoríaForm(request.POST)
            if formulario.is_valid():
                formulario.save()
        except Exception as e:
            mensaje = str(e)
    subcategorías = SubCategoría.objects.all()
    return render(request, 'subcategoría/index.html', {'formulario' : SubCategoríaForm, 'mensaje' : mensaje,'subcategorías' : subcategorías,})


def prioridad(request):
    mensaje = None
    if request.POST:
        try:
            formulario = PrioridadForm(request.POST)
            if formulario.is_valid():
                formulario.save()
        except Exception as e:
            mensaje = str(e)
    prioridades = Prioridad.objects.all()
    return render(request, 'prioridad/index.html', {'formulario' : PrioridadForm, 'mensaje' : mensaje,'prioridades' : prioridades,})


def editar_eliminar_prioridad(request, id):
    mensaje = None
    prioridad = Prioridad.objects.get(pk = id)
    formulario = PrioridadForm(instance=prioridad)
    if request.POST:
        try:
            accion = request.POST.get('acciones')
            if accion == 'editar':            
                formulario = PrioridadForm(request.POST, instance=prioridad)
                if formulario.is_valid():
                    formulario.save()
            elif accion == 'eliminar':
                prioridad.delete()
            return redirect('Prioridad')
        except Exception as e:
            mensaje = str(e)
    return render(request, 'prioridad/editar-eliminar.html', {'mensaje' : mensaje,'formulario' : formulario,})


def cargar_subcategorías(request):
    id_categoría = request.GET.get('id_categoría')
    print(id_categoría)
    subcategorías = SubCategoría.objects.filter(id_categoría=id_categoría).values('id_subcategoría', 'nombre_subCat')
    print(subcategorías)
    return JsonResponse(list(subcategorías), safe=False)


def crear_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Index')
    else:
        form = TicketForm()
    return render(request, 'ticket/crear_ticket.html', {'form': form})