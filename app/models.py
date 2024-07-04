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