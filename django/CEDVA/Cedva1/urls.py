from django.urls import path
from Cedva1 import views

urlpatterns = [
	path('', views.index, name='index'),
	path('2/',views.inicio,name='inicio'),
	path('3/',views.alumnos,name='alumnos'),
	path('4/',views.Ralumnos,name='Ralumnos'),
	path('5/',views.pagos,name='pagos'),
	path('6/',views.pagosP,name='pagosP'),
	path('7/',views.pagosA,name='pagosA'),

]