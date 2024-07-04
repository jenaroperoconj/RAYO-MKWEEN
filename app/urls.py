from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('index/', views.index, name='index'),
    path('main/', views.main, name="main"),
    path('atenciones/', views.atenciones, name="atenciones"),
    path('carrito/', views.carrito, name="carrito"),
    path('rev-postulaciones/', views.rev_postulaciones, name="rev_postulaciones"),
    path('trabaja-con-nosotros/', views.trabaja_con_nosotros, name='trabaja_con_nosotros'),
    path('añadir-postulante/', views.añadirpostulante, name="añadirpostulante"),
    path('eliminar-postulante/<str:rut>/', views.eliminarpostulante, name="eliminarpostulante"),
    path('actualizar-postulante/<str:rut>', views.actualizarpostulante, name="actualizarpostulante"),
    path('actualizar-postulante/editarpostulante/<str:rut>/', views.editarpostulante, name="editarpostulante"),
    path('tienda/', views.tienda, name="tienda"),
    path('añadir-atencion/', views.añadiratencion, name="añadiratencion"),
    path('rev-atenciones/', views.rev_atenciones, name="rev_atenciones"),
]