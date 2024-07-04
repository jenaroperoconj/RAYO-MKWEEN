from django.urls import path
from .views import login, main, atenciones, carrito, revatenciones, trabaja_con_nosotros, index

urlpatterns = [
    path('', login, name="login"),
    path('main/', main, name="main"),
    path('atenciones/', atenciones, name="atenciones"),
    path('carrito/', carrito, name="carrito"),
    path('revatenciones/', revatenciones, name="revatenciones"),
    path('trabaja_con_nosotros/', trabaja_con_nosotros, name='trabaja_con_nosotros'),
    path('index/', index, name='index'),
]