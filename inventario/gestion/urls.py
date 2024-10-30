from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_articulos, name='listar_articulos'),
    path('articulo/nuevo/', views.crear_articulo, name='crear_articulo'),
    path('articulo/editar/<int:pk>/', views.editar_articulo, name='editar_articulo'),
    path('articulo/eliminar/<int:pk>/', views.eliminar_articulo, name='eliminar_articulo'),
    #path('categoria/nuevo/', views.crear_categoria, name='crear_categoria'),
    #path('ubicaion/nuevo/', views.crear_ubicacion, name='crear_ubicacion'),
    path('gestion/listar_ubicaciones.html', views.listar_ubicaciones, name='listar_ubicaciones'),
    path('ubicaciones/', views.listar_ubicaciones, name='listar_ubicaciones'),
    path('ubicaciones/nueva/', views.crear_ubicacion, name='crear_ubicacion'),
    path('ubicaciones/editar/<int:pk>/', views.editar_ubicacion, name='editar_ubicacion'),
    path('ubicaciones/eliminar/<int:pk>/', views.eliminar_ubicacion, name='eliminar_ubicacion'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/nueva/', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:pk>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', views.eliminar_categoria, name='eliminar_categoria'),
    
    
    # Añade aquí las demás rutas necesarias
]
