from django.db import models

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
    id_producto = models.AutoField(db_column='id_producto', primary_key=True)
    nom_producto = models.CharField(max_length=50)
    precio = models.IntegerField()
    categoria = models.IntegerField(choices=categoria_producto, default=0)
    def __str__(self):
        return str(self.id_producto)