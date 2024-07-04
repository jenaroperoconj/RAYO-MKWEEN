from django.shortcuts import render
from .models import Alumno,Genero

# Create your views here.
def index(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'app/alumnos/index.html')

def login(request):
    return render(request,'app/login.html')

def main(request):
    return render(request,'app/main/main.html')

def atenciones(request):
    return render(request,'app/atenciones/atenciones.html')

def carrito(request):
    return render(request,'app/carrito/carrito.html')

def revatenciones(request):
    return render(request,'app/rev-atenciones/revatenciones.html')

def trabaja_con_nosotros(request):
    return render(request, 'app/TrabajaConNosotros/formulario_test.html')