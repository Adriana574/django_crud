from django.urls import path
from AlumnosAdmin import views

urlpatterns = [
    path('alumnos', views.AlumnoListView.as_view(), name="alumnos"),
    path('crearTutor', views.TutorCreateView.as_view(), name="crearTutor"), 
    path('<int:pk>/ver', views.ver.as_view(), name="ver"), 
    path('<int:pk>/update',views.Actualizar.as_view(),name='actualiza'),
    path('<int:pk>/delete',views.Eliminar.as_view(),name='elimina'),
    path('registro', views.registro, name="registro"),   
]