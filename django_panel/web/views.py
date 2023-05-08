from django.shortcuts import render, redirect

# importamos la clase View
from django.views import View
from .models import *
from .forms import *

# Create your views here.
class AlumnoView(View):
    
    def get(self,request):
        listaAlumnos = TblAlumno.objects.all()
        formAlumno = AlumnoForm()
        context = {
            'alumnos' : listaAlumnos,
            'formAlumno': formAlumno
        }
        return render(request,'index.html',context)

    def post(self, request):
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            formAlumno.save()
            return redirect('/')
        
        alumno_id = request.POST.get('alumno_id')
        if alumno_id:
            TblAlumno.objects.filter(pk=alumno_id).delete()
            return redirect('/')
        
class ProfesorView(View):
    def get(self,request):
        listaProfesores = TblProfesor.objects.all()
        formProfesor = ProfesorForm()
        context = {
            'profesores' : listaProfesores,
            'formProfesor' : formProfesor
        }
        return render (request,'profesores.html',context)
    
    def post(self, request):
        formProfesor = ProfesorForm(request.POST)
        if formProfesor.is_valid():
            formProfesor.save()
            return redirect('/')
        
        profesor_id = request.POST.get('profesor_id')
        if profesor_id:
            TblProfesor.objects.filter(pk=profesor_id).delete()
            return redirect('/profesor/')

