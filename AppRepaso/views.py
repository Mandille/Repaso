from django.shortcuts import render
from .models import Curso 
from django.http import HttpResponse

# Create your views here.

def curso(request): #defino la vista curso

    curso1 = Curso(nombre="Js",comision=34656)
    curso1.save()

    curso2 = Curso(nombre="CSS",comision=34658)
    curso2.save()

    lista_cursos=[curso1,curso2]

    cadena_texto = "Curso guardado: "+curso1.nombre+" "+str(curso1.comision)

    return render(request,"AppRepaso/curso.html", {"cursos":lista_cursos})
    return HttpResponse(cadena_texto)


