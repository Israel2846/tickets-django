from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout

# Create your views here.


def inicio_sesion(request):
    mensaje = None
    if request.POST:
        print(request.POST)
        num_empleado = request.POST['num_empleado']
        password = request.POST['password']

        try:
            usuario = authenticate(
                request, num_empleado=num_empleado, password=password)

            if usuario is not None:
                login(request, usuario)
                return redirect('Inicio')
            else:
                return HttpResponse('Credenciales incorrectas')

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


def categoría(request, id=None):
    mensaje = None
    if id:
        categoría = Categoría.objects.get(pk=id)
        formulario = CategoríaForm(instance=categoría)
        if request.POST:
            try:
                accion = request.POST.get('acciones')
                if accion == 'editar':
                    formulario = CategoríaForm(
                        request.POST, instance=categoría)
                    if formulario.is_valid():
                        formulario.save()
                elif accion == 'eliminar':
                    categoría.delete()
                return redirect('Categoría')
            except Exception as e:
                mensaje = str(e)
        return render(request, 'categoría/editar-eliminar.html', {'mensaje': mensaje, 'formulario': formulario, })
    else:
        if request.POST:
            try:
                formulario = CategoríaForm(request.POST)
                if formulario.is_valid():
                    formulario.save()
            except Exception as e:
                mensaje = str(e)
        categorías = Categoría.objects.all()
        return render(request, 'categoría/index.html', {'formulario': CategoríaForm, 'mensaje': mensaje, 'categorías': categorías, })


def subcategoría(request, id=None):
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
                elif accion == 'eliminar':
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
        subcategorías = SubCategoría.objects.all()
        return render(request, 'subcategoría/index.html', {'formulario': SubCategoríaForm, 'mensaje': mensaje, 'subcategorías': subcategorías, })


def cargar_subcategorías(request):
    id_categoría = request.GET.get('id_categoría')
    print(id_categoría)
    subcategorías = SubCategoría.objects.filter(
        id_categoría=id_categoría).values('nombre_subCat', 'id_subcategoría')
    print(subcategorías)
    return JsonResponse(list(subcategorías), safe=False)


def prioridad(request, id=None):
    mensaje = None
    if id:
        prioridad = Prioridad.objects.get(pk=id)
        formulario = PrioridadForm(instance=prioridad)
        if request.POST:
            try:
                accion = request.POST.get('acciones')
                if accion == 'editar':
                    formulario = PrioridadForm(
                        request.POST, instance=prioridad)
                    if formulario.is_valid():
                        formulario.save()
                elif accion == 'eliminar':
                    prioridad.delete()
                return redirect('Prioridad')
            except Exception as e:
                mensaje = str(e)
        return render(request, 'prioridad/editar-eliminar.html', {'mensaje': mensaje, 'formulario': formulario, })
    else:
        if request.POST:
            try:
                formulario = PrioridadForm(request.POST)
                if formulario.is_valid():
                    formulario.save()
            except Exception as e:
                mensaje = str(e)
        prioridades = Prioridad.objects.all()
        return render(request, 'prioridad/index.html', {'formulario': PrioridadForm, 'mensaje': mensaje, 'prioridades': prioridades, })


def ticket(request, id=None):
    if id:
        pass
    mensaje = None

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
