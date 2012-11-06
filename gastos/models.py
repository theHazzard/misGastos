from django.db import models

# Create your models here.
class Tipo(models.model):
	Descripcion = models.CharField(max_length = 100)

class Gasto(models.model):
	usuario = models.ForeignKey(User)
	fecha = models.DateTimeField()
	tipoid = models.ForeignKey(Tipo)
	monto = models.DecimalField()