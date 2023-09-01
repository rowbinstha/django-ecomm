# Generated by Django 4.2.4 on 2023-09-01 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ad",
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
                ("name", models.CharField(max_length=256)),
                ("image", models.ImageField(upload_to="media")),
                ("description", models.TextField()),
                ("rank", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Brand",
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
                ("name", models.CharField(max_length=256)),
                ("image", models.ImageField(upload_to="media")),
                ("rank", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=256)),
                ("logo", models.CharField(blank=True, max_length=200)),
                ("slug", models.CharField(max_length=500, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Slider",
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
                ("name", models.CharField(max_length=256)),
                ("image", models.ImageField(upload_to="media")),
                ("description", models.TextField(blank=True)),
                ("rank", models.IntegerField()),
                ("url", models.URLField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=256)),
                ("price", models.IntegerField()),
                ("discounted_price", models.IntegerField(default=0)),
                ("image", models.ImageField(upload_to="media")),
                ("description", models.TextField(blank=True)),
                ("specification", models.TextField(blank=True)),
                (
                    "stock",
                    models.CharField(
                        choices=[
                            ("in_stock", "In Stock"),
                            ("out of stock", "Out of stock"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "label",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("", "default"),
                            ("new", "New"),
                            ("sale", "Sale"),
                            ("hot", "Hot"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.brand"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.category"
                    ),
                ),
            ],
        ),
    ]
