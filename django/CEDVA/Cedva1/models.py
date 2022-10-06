from django.db import models


class Tutor(models.Model):
	idtutor=models.BigAutoField(primary_key=True,  blank=False)
	nombre=models.CharField(max_length=100)
	apellidoP=models.CharField(max_length=100)
	apellidoM=models.CharField(max_length=100)
	telefono=models.CharField(max_length=100)

	def __unicode__():
         return '{}'.format(self.idtutor)


class Direccion(models.Model):
	iddireccion=models.BigAutoField(primary_key=True,  blank=False)
	calle=models.CharField(max_length=100)
	lote=models.IntegerField()
	manzana=models.IntegerField()
	colonia=models.CharField(max_length=100)
	delegacionMunicipio=models.CharField(max_length=100)
	codigopostal=models.IntegerField()
	ciudadOestado=models.CharField(max_length=100)


class Usuario(models.Model):
	idusuario=models.BigAutoField(primary_key=True,  blank=False)
	user=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	tipo=models.IntegerField()
		

class Escuela(models.Model):
	idescuela=models.BigAutoField(primary_key=True)
	plantel=models.CharField(max_length=100)



class Especialidad(models.Model):
	idespecialidad=models.BigAutoField(primary_key=True)
	idescuela = models.ForeignKey(Escuela,related_name="subcategories8",blank=True , null= True, on_delete=models.CASCADE)
	nombre=models.CharField(max_length=100)
			
						

class Administrador(models.Model):
	idadministrador=models.BigAutoField(primary_key=True,  blank=False)
	idescuela = models.ForeignKey(Escuela,related_name="subcategories5",blank=True , null= True, on_delete=models.CASCADE)
	idusuario= models.ForeignKey(Usuario,related_name="subcategories6",blank=True , null= True, on_delete=models.CASCADE )
	nombre=models.CharField(max_length=100)
	apellidoP=models.CharField(max_length=100)
	apellidoM=models.CharField(max_length=100)		
	
			
class Alumno(models.Model):
	idalumno = models.BigAutoField(primary_key=True)
	idescuela = models.ForeignKey(Escuela, related_name="subcategories",blank=True , null= True, on_delete=models.CASCADE )
	idespecialidad = models.ForeignKey(Especialidad,related_name="subcategories1",blank=True , null= True, on_delete=models.CASCADE )
	iddireccion= models.ForeignKey(Direccion,related_name="subcategories2",blank=True , null= True, on_delete=models.CASCADE )
	idtutor= models.ForeignKey(Tutor,related_name="subcategories3",blank=True , null= True, on_delete=models.CASCADE )
	idusuario= models.ForeignKey(Usuario,related_name="subcategories4",blank=True , null= True, on_delete=models.CASCADE )
	matricula=models.CharField(max_length=100,blank=True)
	nombre=models.CharField(max_length=100)
	apellidoP=models.CharField(max_length=100)
	apellidoM=models.CharField(max_length=100)
	edad=models.IntegerField()
	convenio=models.CharField(max_length=800)
	inicioCurso=models.DateField()
	finalCurso=models.DateField()
	observaciones=models.CharField(max_length=1000)
								

class Pago(models.Model):
	idpago=models.BigAutoField(primary_key=True)
	idalumno = models.ForeignKey(Alumno, related_name="subcategories7",blank=True , null= True, on_delete=models.CASCADE )
	#folio=models.IntegerField()
	tipoPago=models.CharField(max_length=100)
	#monto=models.IntegerField()
	#fechaPago=models.DateField()
	mesPagado=models.CharField(max_length=12)
	#horapago=models.DateTimeField()													