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
from Cedva1.models import *
from django.views.generic import DetailView
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.base import TemplateView
from django.urls import reverse

    
@staff_member_required  
def alumnos(request):
    return render(request, "alumnos.html")

class ver(TemplateView):
    template_name='ver.html'

    def get_context_data(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['Tutor'] = Tutor.objects.get(pk=pk)
        context['Direccion'] = Direccion.objects.get(pk=pk)
        context['Alumno'] = Alumno.objects.get(pk=pk)
        return context 
 
@staff_member_required 
def registro(request):
    return render(request, "registroAlumno.html")   

class TutorCreateView(CreateView):
    template_name='crearTutor.html'
    model = Tutor
    fields ="__all__"


#@login_required(login_url="/loginuser/") 
class AlumnoListView(ListView):
    model = Alumno
    template_name='alumnos.html'
    context_object_name='listas'

class Actualizar(UpdateView):
    model=Alumno
    template_name='actualiza.html'
    context_object_name='cancion'
    fields=('nombreA', 'apellidoPA', 'apellidoMA')

    def get_success_url(self):
        return reverse('alumnos')


class Eliminar(DeleteView):
    model=Alumno
    template_name='AlumnoElimina.html'
    success_url=reverse_lazy('alumnos')

    def get_success_url(self):
        return reverse('alumnos')
    
class AlumnoListView(ListView):
    model = Alumno
    template_name='alumnos.html'
    context_object_name='listas'