from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_articulos, name='listar_articulos'),
    path('articulo/nuevo/', views.crear_articulo, name='crear_articulo'),
    path('articulo/editar/<int:pk>/', views.editar_articulo, name='editar_articulo'),
    path('articulo/eliminar/<int:pk>/', views.eliminar_articulo, name='eliminar_articulo'),
    path('categoria/nuevo/', views.crear_categoria, name='crear_categoria'),
    path('ubicaion/nuevo/', views.crear_ubicacion, name='crear_ubicacion'),
    # Añade aquí las demás rutas necesarias
]
