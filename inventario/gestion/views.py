from django.shortcuts import render, get_object_or_404, redirect
from .models import Articulo 
from .models import Categoria
from .models import Ubicacion
from .forms import ArticuloForm
from .forms import CategoriaForm
from .forms import UbicacionForm
from django.db.models import Q

def listar_articulos(request):
    query = request.GET.get('q')
    if query:
        articulos = Articulo.objects.filter(
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query) |
            Q(categorias__nombre__icontains=query) |
            Q(ubicacion__nombre__icontains=query)
        ).distinct()
    else:
        articulos = Articulo.objects.all()
    return render(request, 'gestion/listar_articulos.html', {'articulos': articulos})
def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_articulos')
    else:
        form = ArticuloForm()
    return render(request, 'gestion/form_articulo.html', {'form': form})

def editar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('listar_articulos')
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'gestion/form_articulo.html', {'form': form})

def eliminar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        articulo.delete()
        return redirect('listar_articulos')
    return render(request, 'gestion/confirmar_eliminacion.html', {'obj': articulo})


def crear_ubicacion(request):
    if request.method == 'POST':
        form = UbicacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_ubicaciones')
    else:
        form = UbicacionForm()
    return render(request, 'gestion/form_ubicacion.html', {'form': form})

def listar_ubicaciones(request):
    ubicaciones_raiz = Ubicacion.objects.filter(padre__isnull=True)  # Ubicaciones raíz (sin padre)
    return render(request, 'gestion/listar_ubicaciones.html', {'ubicaciones_raiz': ubicaciones_raiz})

def editar_ubicacion(request, pk):
    ubicacion = get_object_or_404(Ubicacion, pk=pk)
    if request.method == 'POST':
        form = UbicacionForm(request.POST, instance=ubicacion)
        if form.is_valid():
            form.save()
            return redirect('listar_ubicaciones')  # Redirige al listado de ubicaciones
    else:
        form = UbicacionForm(instance=ubicacion)
    
    return render(request, 'gestion/editar_ubicacion.html', {'form': form, 'ubicacion': ubicacion})

def eliminar_ubicacion(request, pk):
    ubicacion = get_object_or_404(Ubicacion, pk=pk)
    if request.method == 'POST':
        ubicacion.delete()
        return redirect('listar_ubicaciones')  # Redirige al listado de ubicaciones
    
    return render(request, 'gestion/eliminar_ubicacion.html', {'ubicacion': ubicacion})


def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'gestion/listar_categorias.html', {'categorias': categorias})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    
    return render(request, 'gestion/crear_categoria.html', {'form': form})

def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'gestion/editar_categoria.html', {'form': form, 'categoria': categoria})

def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')
    
    return render(request, 'gestion/eliminar_categoria.html', {'categoria': categoria})






