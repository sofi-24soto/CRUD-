from django.shortcuts import redirect, render
from .models import Curso


# Create your views here.

def home(request):
    cursos = Curso.objects.all()
    return render(request, "gestionCurso.html", {"cursos": cursos})

def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    curso=Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')

def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    return redirect('/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')