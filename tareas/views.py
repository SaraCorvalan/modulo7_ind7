from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from tareas.models import registroTareas
from .forms import registroForm, LoginForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# TAREAS

def tareas(request):
    return render(request, 'landing.html')


@login_required
def formularioRegistroTareas(request):
    tareas = registroTareas.objects.all().order_by('id_tarea')
    for t in tareas:
        ultima_tarea = t.id_tarea
    data = {
        'form': registroForm(),
        'ultima': ultima_tarea
    }
    if request.method == 'POST':
        formulario = registroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "TAREA REGISTRADA !!!"
        else:
            data["form"] = formulario
    print("************************************************************************************")   
    print("ultima_tarea: ", ultima_tarea)
    print("************************************************************************************")   
    return render(request, 'registro_tareas.html', data)


@login_required
def administraTareasEstado(request):
    tareas = registroTareas.objects.all().order_by('estado_tarea')
    return render(request, 'administra_tareas_estado.html', {'tareas': tareas})

@login_required
def administraTareasTarea(request):
    tareas = registroTareas.objects.all().order_by('id_tarea')
    return render(request, 'administra_tareas_tarea.html', {'tareas': tareas})

@login_required
def administraTareasVencimiento(request):
    tareas = registroTareas.objects.all().order_by('fecha_vencimiento_tarea')
    return render(request, 'administra_tareas_vencimiento.html', {'tareas': tareas})

@login_required
def modificaTareas(request, id):
    tarea = registroTareas.objects.get(pk = id) 
    data = {
        'form': registroForm(instance=tarea)
    }
    if request.method == 'POST':
        formulario = registroForm(data=request.POST, instance=tarea)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "TAREA MODIFICADA !!!"
            return render(request, 'modifica_tareas.html', data)
        else:
            data["form"] = formulario
    return render(request, 'modifica_tareas.html', data)


@login_required
def eliminaTareas(request, id):
    tarea_elimina = registroTareas.objects.get(pk = id)
    tarea_elimina.delete()
    return render(request, 'elimina_tareas.html', {'tarea': id})


@login_required
def completaTareas(request, id):
    tarea_a_completar = registroTareas.objects.get(pk = id)
    tarea_a_completar.estado_tarea = "3"
    tarea_a_completar.save()
    tareas = registroTareas.objects.all().order_by('estado_tarea')
    return render(request, 'completa_tareas.html', {'tareas': tareas})

##############################################################################################


# USUARIOS
def user_login(request):
    
    if request.method == 'POST':
        formulario = LoginForm(data=request.POST)
        if formulario.is_valid():
           usuario = formulario.cleaned_data['usuario']
           password = formulario.cleaned_data['password']
           user = authenticate(request, username=usuario, password=password)
           if user is not None:
               if user.is_active:
                   login(request, user)
                   #messages.success(request, f"Autentificación exitosa, estimado(a) {usuario}")
                   return render(request, 'registration/bienvenida.html', {'users': usuario})
                   #return HttpResponse(f"Autentificación exitosa, estimado(a) {usuario}")
               else:
                   messages.error(request, "Cuenta no habilitada")
                   #return HttpResponse("Cuenta NO habilitada")
           else:
               #return HttpResponse("Login No válido")
                messages.error(request, "Login no válido")
    else:
        formulario = LoginForm()

    return render(request, 'registration/login.html', {'formulario': formulario})


              

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }   
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
           formulario.save()
           usuario = formulario.cleaned_data['username']
           password = formulario.cleaned_data['password1']
           user = authenticate(request, username=usuario, password=password)       
           login(request, user)
           return render(request, 'registration/bienvenida.html', {'users': usuario})
           messages.success(request, f"Te has registrado correctamente, estimado(a) {usuario}")           
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)
