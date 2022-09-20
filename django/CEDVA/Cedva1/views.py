from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'index.html')

def inicio(request):
	return render(request,'director/inicio.html')	

def alumnos(request):
	return render(request,'director/alumnos.html')	

def Ralumnos(request):
	return render(request,'director/registroAlumno.html')			

def pagos(request):
	return render(request,'director/pagos.html')	

def pagosP(request):
	return render(request,'director/pagosPeriodo.html')	

def pagosA(request):
	return render(request,'director/pagosAlumno.html')					