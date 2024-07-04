from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import postulacion, atencion, producto, carrito, itemcarrito
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request,'app/login.html')

def index(request):
    return render(request, 'app/index.html')

def main(request):
    return render(request,'app/main.html')

def atenciones(request):
    return render(request,'app/atenciones.html')
@login_required
def carrito_view(request):
    # Inicializar variables
    carritos = None
    itemcarritos = []

    if request.user.is_authenticated:
        # Obtener carrito actual
        carritos, created = carrito.objects.get_or_create(user=request.user, completado=False)
        # Obtener items del carrito actual
        itemcarritos = itemcarrito.objects.filter(carrito=carritos)

    context = {
        'carrito': carritos,
        'itemcarritos': itemcarritos,
    }

    return render(request, 'app/carrito.html', context)

@login_required
def rev_postulaciones(request):
    postulaciones = postulacion.objects.all()

    context = {
        'postulaciones' :postulaciones
    }
    return render(request,'app/rev-postulaciones.html',context)

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

        try:
            postulaciones.save()
            messages.success(request, 'Postulación publicada correctamente.')
        except Exception as exception:
            messages.error(request, f'Error al publicar postulante: {str(exception)}')
    return render(request, 'app/job-w-us.html')

#Filtro para eliminar postulantes por rut
def eliminar_postulante(request,rut):
    postulaciones = postulacion.objects.get(rut=rut)
    try:
        postulaciones.delete()
        messages.success(request, 'Postulante eliminado correctamente.')
    except Exception as exception:
        messages.error(request, f'Error al eliminar postulante: {str(exception)}')

    return redirect("rev_postulaciones")

#Función para filtrar postulantes por rut y enviar los datos a la vista actualizar postulantes
def actualizar_postulante(request,rut):
    postulaciones = postulacion.objects.get(rut=rut)

    context = {
        'postulaciones' :postulaciones
    }
    return render(request, 'app/actualizar-postulaciones.html',context)

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

@login_required
def rev_atenciones(request):
    atenciones = atencion.objects.all()

    context = {
        'atenciones' :atenciones
    }
    return render(request,'app/rev-atenciones.html',context)

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
        try:
            atenciones.save()
            messages.success(request, 'La atención ha sido enviada')
        except Exception as exception:
            messages.error(request, f'Error al enviar la atención: {str(exception)}')
    return render(request, 'app/atenciones.html')

#Eliminar atenciones realizadas
def eliminar_atencion(request, id_atencion):
    atencion_obj = get_object_or_404(atencion, id_atencion=id_atencion)
    try:
        atencion_obj.delete()
        messages.success(request, 'La atención ha sido eliminada correctamente.')
    except Exception as exception:
        messages.error(request, f'Error al eliminar la atención: {str(exception)}')

    return redirect('rev_atenciones')

#Actividad atenciones por id
def actualizar_atencion(request,id_atencion):
    atenciones = atencion.objects.get(id_atencion=id_atencion)

    context = {
        'atenciones' :atenciones
    }
    return render(request, 'app/actualizar-atenciones.html',context)

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
@login_required
def tienda(request):
    productos = producto.objects.all()

    # Obtener el carrito del usuario actual
    user_carrito, created = carrito.objects.get_or_create(user=request.user, completado=False)
    itemcarritos = itemcarrito.objects.filter(carrito=user_carrito)

    context = {
        'productos': productos,
        'itemcarritos': itemcarritos,
        'carrito': user_carrito,
    }
    return render(request, 'app/tienda.html',context)

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

#----------------------------------HECHOS PERO NO IMPLEMENTADOS------------------------------
def eliminar_producto(request,id_producto):
    productos = producto.objects.get(id_producto=id_producto)
    productos.delete()
    return redirect("tienda")

def actualizar_producto(request,id_producto):
    productos = producto.objects.get(id_producto=id_producto)

    context = {
        'productos' :productos
    }
    return render(request, 'app/actualizar-producto.html',context)

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
#--------------------------------FIN DE FUNCIONES OLVIDADAS--------------------------------

#Vista para añadir productos al carrito
def test(request):
    return render(request, 'app/add-product.html')

@login_required
def agregar_al_carrito(request):
    if request.method == 'POST':
        id_producto = request.POST.get('id_producto')
        producto_obj = get_object_or_404(producto, id_producto=id_producto)

        if request.user.is_authenticated:
            carrito_actual, created = carrito.objects.get_or_create(user=request.user, completado=False)
            item, item_created = itemcarrito.objects.get_or_create(carrito=carrito_actual, producto=producto_obj)
            item.cantidad += 1
            item.save()

        return redirect(request.META.get('HTTP_REFERER'))

@login_required
def eliminar_del_carrito(request, id_item):
    item = itemcarrito.objects.get(id=id_item)
    item.delete()
    return redirect('carrito')

@login_required
def quitar_del_carrito(request):
    if request.method == 'POST':
        id_producto = request.POST.get('id_producto')

        if request.user.is_authenticated:
            carritos = carrito.objects.get(user=request.user, completado=False)
            item = itemcarrito.objects.get(carrito=carritos, producto=id_producto)
            if item.cantidad > 1:
                item.cantidad -= 1
                item.save()
            else:
                item.delete()

        return redirect('tienda')