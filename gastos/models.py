from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tipo(models.Model):
	Descripcion = models.CharField(max_length = 100)

class Gasto(models.Model):
	usuario = models.ForeignKey(User)
	fecha = models.DateTimeField()
	tipoid = models.ForeignKey(Tipo)
	monto = models.DecimalField(max_digits=9, decimal_places=2)