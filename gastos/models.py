from django.db import models

# Create your models here.
class Tipo(models.Model):
	Descripcion = models.CharField(max_length = 100)

class Gasto(models.Model):
	usuario = models.ForeignKey(User)
	fecha = models.DateTimeField()
	tipoid = models.ForeignKey(Tipo)
	monto = models.DecimalField()