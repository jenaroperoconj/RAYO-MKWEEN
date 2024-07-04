from django.contrib import admin
from .models import postulacion, atencion, producto, carrito, itemcarrito
# Register your models here.
admin.site.register(postulacion)
admin.site.register(atencion)
admin.site.register(producto)
admin.site.register(carrito)
admin.site.register(itemcarrito)