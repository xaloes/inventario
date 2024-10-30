# Generated by Django 5.1.2 on 2024-10-30 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Ubicacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Articulo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("descripcion", models.TextField()),
                ("foto", models.ImageField(upload_to="articulos/")),
                ("unidades", models.PositiveIntegerField()),
                ("categorias", models.ManyToManyField(to="gestion.categoria")),
                (
                    "ubicacion",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="gestion.ubicacion",
                    ),
                ),
            ],
        ),
    ]
