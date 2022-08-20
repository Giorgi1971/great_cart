# Generated by Django 4.1 on 2022-08-19 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
                ("category_name", models.CharField(max_length=50)),
                ("slug", models.CharField(max_length=100, unique=True)),
                ("description", models.CharField(blank=True, max_length=255)),
                (
                    "cat_image",
                    models.ImageField(blank=True, upload_to="photos/categories/"),
                ),
            ],
            options={"verbose_name": "category", "verbose_name_plural": "categories",},
        ),
    ]