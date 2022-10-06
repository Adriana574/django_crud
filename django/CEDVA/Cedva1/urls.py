from django.urls import path
from Cedva1 import views

urlpatterns = [
    path('loginuser/', views.LoginUser, name="loginuser"),
    path('homepage', views.HomePage, name="homepage"),
    path('alumnos', views.AlumnoListView.as_view(), name="alumnos"),
    path('<int:pk>/update',views.Actualizar.as_view(),name='actualiza'),
    path('<int:pk>/delete',views.Eliminar.as_view(),name='elimina'),
    path('pagos', views.AlumnoPListView.as_view(), name="pagos"),
    path('registro', views.registro, name="registro"),
    path('pagoalumno', views.AlumnoPagoListView.as_view(), name="pagoalumno"),
    path('<int:pk>/pago',views.Actualizarpago.as_view(),name='actualizaP'),
    path('logout/', views.LogoutUser, name="logout"),
    path('clicklogin', views.clicklogin, name="clicklogin"),
    path('',views.LoginUser,name=""),
]