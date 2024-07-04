from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
opciones_genero = [
    [0,"Seleccione"],
    [1,"Femenino"],
    [2,"Masculino"],
    [3,"Helicoptera"],
]

class postulacion(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    pnombre = models.CharField(max_length=50)
    appaterno = models.CharField(max_length=50)
    apmaterno = models.CharField(max_length=50)
    edad = models.IntegerField()
    tipo_genero = models.IntegerField(choices=opciones_genero, default=0)
    email = models.EmailField(max_length=100, blank=True, null=False)
    celular = models.IntegerField()
    especializacion = models.CharField(max_length=50)
    motivo = models.TextField()

    def __str__(self):
        return str(self.rut)

categoria_opc = [
    [0,"Seleccione"],
    [1,"Mantención"],
    [2,"Cambio de pieza"],
    [3,"Limpieza"],
]
class atencion(models.Model):
    id_atencion = models.AutoField(db_column='id_atencion', primary_key=True)
    nom_mecanico = models.CharField(max_length=50)
    nom_cliente = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=False)
    fecha_atencion = models.DateField()
    categoria = models.IntegerField(choices=categoria_opc, default=0)
    descripcion = models.TextField()

    def __str__(self):
        return str(self.id_atencion)

categoria_producto = [
    [0,"Seleccione"],
    [1,"Ruedas"],
    [2,"Suspensiones"],
    [3,"Turbos"],
    [4,"Frenos"],
]

class producto(models.Model):
    id_producto = models.AutoField(db_column='id_producto',primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria_prod = models.IntegerField(choices=categoria_producto, default=0)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre

class carrito(models.Model):
    id_carrito = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id_carrito)

    @property
    def precio_total(self):
        itemcarritos = self.itemcarrito_set.all()
        total = sum(item.precio for item in itemcarritos)
        return total

class itemcarrito(models.Model):
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(carrito, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.producto.nombre

    @property
    def precio(self):
        nuevo_precio = self.producto.precio * self.cantidad
        return nuevo_precio