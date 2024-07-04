from django.urls import path
from . import views

from django.urls import path, include

urlpatterns = [
    path('', views.main, name="main"),
    path('atenciones/', views.atenciones, name="atenciones"),
    path('carrito/', views.carrito, name="carrito"),
    path('rev-postulaciones/', views.rev_postulaciones, name="rev_postulaciones"),
    path('job-w-us/', views.trabaja_con_nosotros, name='trabaja_con_nosotros'),
    path('añadir-postulante/', views.publicar_postulante, name="añadirpostulante"),
    path('eliminar-postulante/<str:rut>/', views.eliminar_postulante, name="eliminarpostulante"),
    path('actualizar-postulante/<str:rut>', views.actualizar_postulante, name="actualizarpostulante"),
    path('actualizar-postulante/editarpostulante/<str:rut>/', views.editar_postulante, name="editarpostulante"),
    path('rev-atenciones/', views.rev_atenciones, name="rev_atenciones"),
    path('añadir-atencion/', views.publicar_atencion, name="añadiratencion"),
    path('eliminar-atencion/<int:id_atencion>/', views.eliminar_atencion, name="eliminaratencion"),
    path('actualizar-atencion/<int:id_atencion>/', views.actualizar_atencion, name="actualizaratencion"),
    path('editar-atencion/<int:id_atencion>/', views.editar_atencion, name="editaratencion"),
    path('tienda/', views.tienda, name="tienda"),
    path('añadir-producto/', views.publicar_producto, name="añadirproducto"),
    path('eliminar-producto/<int:id_producto>/', views.eliminar_producto, name="eliminarproducto"),
    path('actualizar-producto/<int:id_producto>/', views.actualizar_producto, name="actualizarproducto"),
    path('editar-producto/<int:id_producto>/', views.editar_producto, name="editarproducto"),
    path('test/', views.test, name="test"),
    
]