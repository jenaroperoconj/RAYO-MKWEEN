from django.shortcuts import render, redirect
from .models import postulacion, atencion, producto

# Create your views here.
def login(request):
    return render(request,'app/login.html')

def index(request):
    return render(request, 'app/index.html')

def main(request):
    return render(request,'app/main.html')

def atenciones(request):
    return render(request,'app/atenciones.html')

def carrito(request):
    return render(request,'app/carrito.html')

def rev_postulaciones(request):
    postulaciones = postulacion.objects.all()
    return render(request,'app/rev-postulaciones.html',{'postulaciones' :postulaciones})

def trabaja_con_nosotros(request):
    return render(request, 'app/job-w-us.html')

#Función para añadir postulantes
def publicar_postulante(request):
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
        #Luego de obtener los datos, se crea un objeto postulaciones llamando al modelo postulaciones
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
    return render(request, 'app/job-w-us.html')

#Filtro para eliminar postulantes por rut
def eliminar_postulante(request,rut):
    postulaciones = postulacion.objects.get(rut=rut)
    postulaciones.delete()
    return redirect("rev_postulaciones")

#Función para filtrar postulantes por rut y enviar los datos a la vista actualizar postulantes
def actualizar_postulante(request,rut):
    postulaciones = postulacion.objects.get(rut=rut)
    return render(request, 'app/actualizar-postulaciones.html',{'postulaciones':postulaciones})

#Obtiene los postulantes por rut y envia los datos a revisar postulaciones
def editar_postulante(request,rut):
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

def rev_atenciones(request):
    atenciones = atencion.objects.all()
    return render(request,'app/rev-atenciones.html',{'atenciones' :atenciones})

def publicar_atencion(request):
    if request.method == 'POST':
        nom_mecanico = request.POST.get('nom_mecanico')
        nom_cliente = request.POST.get('nom_cliente')
        email = request.POST.get('email')
        fecha_atencion = request.POST.get('fecha_atencion')
        categoria = request.POST.get('categoria')
        descripcion = request.POST.get('descripcion')

        atenciones = atencion(
            nom_mecanico=nom_mecanico,
            nom_cliente=nom_cliente,
            email=email,
            fecha_atencion=fecha_atencion,
            categoria=categoria,
            descripcion=descripcion)
        atenciones.save()
    return render(request, 'app/atenciones.html')

#Eliminar atenciones realizadas
def eliminar_atencion(request,id_atencion):
    atenciones = atencion.objects.get(id_atencion=id_atencion)
    atenciones.delete()
    return redirect("rev_atenciones")

#Actividad atenciones por id
def actualizar_atencion(request,id_atencion):
    atenciones = atencion.objects.get(id_atencion=id_atencion)
    return render(request, 'app/actualizar-atenciones.html',{'atenciones':atenciones})

def editar_atencion(request,id_atencion):
    id_atencion = request.POST['id_atencion']
    nom_mecanico = request.POST['nom_mecanico']
    nom_cliente = request.POST['nom_cliente']
    email = request.POST['email']
    fecha_atencion = request.POST['fecha_atencion']
    categoria = request.POST['categoria']
    descripcion = request.POST['descripcion']

    atenciones = atencion.objects.get(id_atencion=id_atencion)
    atenciones.id_atencion = id_atencion
    atenciones.nom_mecanico = nom_mecanico
    atenciones.nom_cliente = nom_cliente
    atenciones.email = email
    atenciones.fecha_atencion = fecha_atencion
    atenciones.categoria = categoria
    atenciones.descripcion = descripcion
    atenciones.save()
    return redirect("rev_atenciones")

def tienda(request):
    productos = producto.objects.all()
    return render(request, 'app/tienda.html',{'productos' :productos})

def publicar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        imagen = request.FILES.get('imagen')

        productos = producto(nombre=nombre,
                            descripcion=descripcion, 
                            precio=precio, 
                            imagen=imagen)
        productos.save()
        return redirect('tienda')
    return render(request, 'app/tienda.html')

def eliminar_producto(request,id_producto):
    productos = producto.objects.get(id_producto=id_producto)
    productos.delete()
    return redirect("tienda")

def actualizar_producto(request,id_producto):
    productos = producto.objects.get(id_producto=id_producto)
    return render(request, 'app/actualizar-producto.html',{'productos':productos})

def editar_producto(request,id_producto):
    id_producto = request.POST['id_producto']
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    categoria_prod = request.POST['categoria_prod']
    precio = request.POST['precio']
    imagen = request.POST['imagen']

    productos = atencion.objects.get(id_producto=id_producto)
    productos.id_producto = id_producto
    productos.nombre = nombre
    productos.descripcion = descripcion
    productos.categoria_prod = categoria_prod
    productos.precio = precio
    productos.imagen = imagen
    productos.save()
    return redirect("tienda")

def test(request):
    return render(request, 'app/add-product.html')