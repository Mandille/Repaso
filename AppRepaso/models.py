from django.db import models

# Create your models here.

# Ahora en mi bdd voy a tener una tabla cursos

class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()

    def __str__(self): 
        return self.nombre+" "+str(self.comision)

