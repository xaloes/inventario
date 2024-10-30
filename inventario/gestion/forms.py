from django import forms
from .models import Articulo, Categoria, Ubicacion

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['nombre', 'descripcion', 'foto', 'unidades', 'categorias', 'ubicacion']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Agrega los atributos al campo de imagen
        self.fields['foto'].widget.attrs.update({
            'accept': 'image/*',
            'capture': 'environment'
        })

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']  # Campos para crear y editar

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['nombre', 'descripcion', 'padre']  # Incluye el campo padre

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Opcional: añade una etiqueta más amigable para el campo padre
        self.fields['padre'].label = "Ubicación Padre"
        self.fields['padre'].required = False  # Permite que el campo sea opcional
