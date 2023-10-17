from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def inicio_sesion(request):
    mensaje = None

    if request.POST:
        num_empleado = request.POST['num_empleado']
        password = request.POST['password']

        try:
            usuario = authenticate(
                request, num_empleado=num_empleado, password=password)

            if usuario is not None:
                login(request, usuario)
                return redirect('Inicio')

            else:
                mensaje = 'Credenciales incorrectas'

        except Exception as e:
            mensaje = str(e)

    return render(request, 'login.html', {'mensaje': mensaje})


def cerrar_sesion(request):
    logout(request)
    return redirect('Login')


def index(request):
    return render(request, 'base.html')


def usuario(request):
    if request.POST:

        if request.POST['password1'] == request.POST['password2']:

            Usuario.objects.create_user(
                nombres_usuario=request.POST['nombres_usuario'],
                appat_usuario=request.POST['appat_usuario'],
                apmat_usuario=request.POST['apmat_usuario'],
                num_empleado=request.POST['num_empleado'],
                num_tel=request.POST['num_tel'],
                email=request.POST['email'],
                rol=request.POST['rol'],
                password=request.POST['password1']
            )

            return redirect('Inicio')

        return HttpResponse('Las contraseñas no coinciden')

    return render(request, 'usuario/index.html', {'formulario': UsuarioForm})


def categoría(request):
    mensaje = None
    categorías = Categoría.objects.all()
    formulario = CategoríaForm()

    if request.POST:
        if 'id_categoría_modal' in request.POST:
            acciones = request.POST['acciones']
            categoría = Categoría.objects.get(
                pk=request.POST['id_categoría_modal'])

            try:
                if acciones == 'aceptar':
                    categoría.nombre_cat = request.POST['modal_nombre']
                    categoría.save()

                elif acciones == 'eliminar':
                    categoría.delete()

                return redirect('Categoría')

            except Exception as e:
                mensaje = str(e)

        try:
            formulario = CategoríaForm(request.POST)

            if formulario.is_valid():
                formulario.save()

        except Exception as e:
            mensaje = str(e)

    if request.GET.get('id_categoría'):
        try:
            id_categoría = request.GET.get('id_categoría')
            categoría = Categoría.objects.get(pk=id_categoría)
            categoría_dicc = model_to_dict(categoría)

            return JsonResponse({"categoría": categoría_dicc})

        except Exception as e:
            mensaje = str(e)

    return render(request, 'categoría/index.html', {'formulario': formulario, 'mensaje': mensaje, 'categorías': categorías, })


def subcategoría(request, id=None):
    subcategorías = SubCategoría.objects.all()
    mensaje = None

    if id:
        subcategoría = SubCategoría.objects.get(pk=id)

        if request.POST:
            try:
                accion = request.POST.get('acciones')

                if accion == 'editar':
                    formulario = SubCategoríaForm(
                        request.POST, instance=subcategoría)

                    if formulario.is_valid():
                        formulario.save()

                if accion == 'eliminar':
                    subcategoría.delete()

                return redirect('Subcategoría')

            except Exception as e:
                mensaje = str(e)

        else:
            formulario = SubCategoríaForm(instance=subcategoría)

        return render(request, 'subcategoría/editar-eliminar.html', {'mensaje': mensaje, 'formulario': formulario})

    else:
        if request.POST:
            try:
                formulario = SubCategoríaForm(request.POST)

                if formulario.is_valid():
                    formulario.save()

            except Exception as e:
                mensaje = str(e)

        return render(request, 'subcategoría/index.html', {'formulario': SubCategoríaForm, 'mensaje': mensaje, 'subcategorías': subcategorías, })


def cargar_subcategorías(request):
    id_categoría = request.GET.get('id_categoría')

    subcategorías = SubCategoría.objects.filter(
        id_categoría=id_categoría).values('nombre_subCat', 'id_subcategoría')

    return JsonResponse(list(subcategorías), safe=False)


def prioridad(request):
    prioridades = Prioridad.objects.all()
    mensaje = None
    formulario = PrioridadForm()

    if request.POST:
        if 'id_prioridad_modal' in request.POST:
            acciones = request.POST['acciones']
            prioridad = Prioridad.objects.get(
                pk=request.POST['id_prioridad_modal'])

            try:
                if acciones == "modificar":
                    prioridad.nombre_prioridad = request.POST['modal_nombre']
                    prioridad.save()

                elif acciones == "eliminar":
                    prioridad.delete()

                return redirect('Prioridad')

            except Exception as e:
                mensaje = str(e)

        try:
            formulario = PrioridadForm(request.POST)

            if formulario.is_valid():
                formulario.save()

        except Exception as e:
            mensaje = str(e)

    if request.GET.get('id_prioridad'):
        try:
            prioridad = Prioridad.objects.get(
                pk=request.GET.get('id_prioridad'))
            prioridad_dicc = model_to_dict(prioridad)

            return JsonResponse({'prioridad': prioridad_dicc})

        except Exception as e:
            mensaje = str(e)

    return render(request, 'prioridad/index.html', {'formulario': PrioridadForm, 'mensaje': mensaje, 'prioridades': prioridades, })


def ticket(request, id=None):
    mensaje = None

    if id:
        ticket = Ticket.objects.get(pk=id)
        formulario = TicketForm(instance=ticket)

        if request.POST:
            try:
                formulario = TicketForm(
                    request.POST, request.FILES, instance=ticket)
                accion = request.POST['acciones']

                if accion == 'guardar':
                    if formulario.is_valid():
                        formulario.save()

                if accion == 'eliminar':
                    ticket.delete()

                return redirect('Consultar tickets')

            except Exception as e:
                mensaje = str(e)

        return render(request, 'ticket/crear_ticket.html', {'formulario': formulario, 'mensaje': mensaje, 'editar': True})

    if request.POST:
        try:
            formulario = TicketForm(request.POST, request.FILES)

            if formulario.is_valid():
                nueva_tarea = formulario.save(commit=False)
                nueva_tarea.usuario_creador = request.user
                nueva_tarea.save()

                return redirect('Inicio')

        except Exception as e:
            mensaje = str(e)

    return render(request, 'ticket/crear_ticket.html', {'formulario': TicketForm, 'mensaje': mensaje})


def consultar_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticket/consultar_tickets.html', {'tickets': tickets})
