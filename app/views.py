from django.shortcuts import render, redirect
from .models import postulacion

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def login(request):
    return render(request,'app/login.html')

def main(request):
    return render(request,'app/main.html')

def atenciones(request):
    return render(request,'app/atenciones.html')

def carrito(request):
    return render(request,'app/carrito.html')

def revatenciones(request):
    return render(request,'app/revatenciones.html')

def rev_postulaciones(request):
    postulaciones = postulacion.objects.all()
    return render(request,'app/rev-postulaciones.html',{'postulaciones' :postulaciones})

def trabaja_con_nosotros(request):
    return render(request, 'app/formulario_test.html')

def tienda(request):
    return render(request, 'app/tienda.html')

def añadirpostulante(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        pnombre = request.POST.get('pnombre')
        appaterno = request.POST.get('appaterno')
        apmaterno = request.POST.get('apmaterno')
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
            edad=edad,
            tipo_genero=tipo_genero,
            email=email,
            celular=celular,
            especializacion=especializacion,
            motivo=motivo
        )
        postulaciones.save()
        return redirect("main")
    return render(request, 'app/formulario_test.html')

def eliminarpostulante(request,rut):
    postulaciones = postulacion.objects.get(rut=rut)
    postulaciones.delete()
    return redirect("rev_postulaciones")

def actualizarpostulante(request,rut):
    postulaciones = postulacion.objects.get(rut=rut)
    return render(request, 'app/actualizar-postulaciones.html',{'postulaciones':postulaciones})

def editarpostulante(request,rut):
    rut = request.POST['rut']
    pnombre = request.POST['pnombre']
    appaterno = request.POST['appaterno']
    apmaterno = request.POST['apmaterno']
    edad = request.POST['edad']
    tipo_genero = request.POST['tipo_genero']
    email = request.POST['email']
    celular = request.POST['celular']
    especializacion = request.POST['especializacion']
    motivo = request.POST['motivo']

    postulaciones = postulacion.objects.get(rut=rut)
    postulaciones.rut = rut
    postulaciones.pnombre = pnombre
    postulaciones.appaterno = appaterno
    postulaciones.apmaterno = apmaterno
    postulaciones.edad = edad
    postulaciones.tipo_genero = tipo_genero
    postulaciones.email = email
    postulaciones.celular = celular
    postulaciones.especializacion = especializacion
    postulaciones.motivo = motivo
    postulaciones.save()
    return redirect("rev_postulaciones")