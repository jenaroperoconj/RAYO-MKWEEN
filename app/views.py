from django.shortcuts import render, redirect
from .models import postulacion

# Create your views here.
def index(request):
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
    postulaciones = postulacion.objects.all()
    return render(request,'app/rev-atenciones/revatenciones.html',{'postulaciones' :postulaciones})

def trabaja_con_nosotros(request):
    return render(request, 'app/TrabajaConNosotros/formulario_test.html')

def añadirpostulante(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        pnombre = request.POST.get('pnombre')
        appaterno = request.POST.get('appaterno')
        apmaterno = request.POST.get('apmaterno')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        edad = request.POST.get('edad')
        tipo_genero = request.POST.get('tipo_genero')
        email = request.POST.get('email')
        celular = request.POST.get('celular')
        especializacion = request.POST.get('especializacion')
        motivo = request.POST.get('motivo')

        postulaciones = postulacion(
            rut=rut,
            pnombre=pnombre,
            appaterno=appaterno,
            apmaterno=apmaterno,
            fecha_nacimiento=fecha_nacimiento,
            edad=edad,
            tipo_genero=tipo_genero,
            email=email,
            celular=celular,
            especializacion=especializacion,
            motivo=motivo
        )
        postulaciones.save()
        return redirect('../main')

    return render(request, 'app/TrabajaConNosotros/formulario_test.html')