from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import * 
from django.contrib.admin.views.decorators import staff_member_required


def LoginUser(request):
    if request.user.username=="":
        return render(request,"index.html")
    else:
        return HttpResponseRedirect("/homepage")

@staff_member_required(login_url="/loginuser/") 
def HomePage(request):
    return render(request, "director/inicio.html")
    

@staff_member_required(login_url="/loginuser/")   
def alumnos(request):
    return render(request, "director/alumnos.html")  


@staff_member_required(login_url="/loginuser/")  
def pagos(request):
    return render(request, "director/pagos.html")  

@staff_member_required(login_url="/loginuser/") 
def registro(request):
    return render(request, "director/registroAlumno.html")            


@staff_member_required(login_url="/loginuser/") 
def pagoalumno(request):
    return render(request, "director/pagosAlumno.html")            


def clicklogin(request):
    if request.method!="POST":
        return HttpResponse("<h1> Methoid not allowed<h1>")
    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        
        user=authenticate(username=username,password=password)
        if user!=None:
            login(request,user)
            if request.user.is_staff:
                return HttpResponseRedirect('/homepage')
            else:      
                return HttpResponseRedirect('1inicio')  
        else:
            messages.error(request, "Invalid Login")
            return HttpResponseRedirect('/')
        

def LogoutUser(request):
    logout(request)
    request.user=None
    return HttpResponseRedirect("/loginuser")            

#@login_required(login_url="/loginuser/") 
class AlumnoListView(ListView):
    model = Alumno
    template_name='director/alumnos.html'
    context_object_name='listas'

class Actualizar(UpdateView):
    model=Alumno
    template_name='director/actualiza.html'
    context_object_name='cancion'
    fields=('nombre', 'apellidoP', 'apellidoM')

class Eliminar(DeleteView):
    model=Alumno
    template_name='director/AlumnoElimina.html'
    success_url=reverse_lazy('alumnos')

class AlumnoPListView(ListView):
    model =Alumno
    template_name='director/pagos.html'
    context_object_name='listas'

class AlumnoPagoListView(ListView):
    model =Pago
    template_name='director/pagosAlumno.html'
    context_object_name='listas'

class Actualizarpago(UpdateView):
    model=Pago
    template_name='director/actualizaPago.html'
    context_object_name='pago' 
    fields=('folio', 'tipoPago', 'monto','fechaPago','mesPagado','horapago')  