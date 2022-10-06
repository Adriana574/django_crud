from django.forms import ModelForm

from . models import *

class DireccionModel(forms.ModelForm):

    class Meta:
        model = Direccion
        fields = ('Calle', 'Lote', 'Manzana', 'Colonia', 'Delegación', 'CP', 'CE',)

class TutorModel(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('Nombre', 'apellido Paterno',)

class AlumnoModel(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('Nombre', 'apellido Paterno',)