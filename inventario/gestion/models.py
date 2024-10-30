from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    categorias = models.ManyToManyField('Categoria', blank=True)  # Relación de muchos a muchos
    
    def __str__(self):
        return self.nombre

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    
    # Relación autorreferencial para jerarquía
    padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='hijos')
    
    def __str__(self):
        # Esto muestra la jerarquía completa en el nombre
        if self.padre:
            return f"{self.padre} > {self.nombre}"
        return self.nombre

    class Meta:
        verbose_name_plural = "Ubicaciones"

class Articulo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='articulos/', blank=True, null= True)
    unidades = models.PositiveIntegerField()
    categorias = models.ManyToManyField(Categoria)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre
    