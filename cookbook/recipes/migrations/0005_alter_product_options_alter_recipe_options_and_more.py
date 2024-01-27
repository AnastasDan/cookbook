# Generated by Django 5.0.1 on 2024-01-27 11:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0004_alter_product_options_alter_recipe_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ("id",),
                "verbose_name": "продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AlterModelOptions(
            name="recipe",
            options={
                "ordering": ("id",),
                "verbose_name": "рецепт",
                "verbose_name_plural": "Рецепты",
            },
        ),
        migrations.AlterModelOptions(
            name="recipeproduct",
            options={
                "ordering": ("id",),
                "verbose_name": "продукт в рецепте",
                "verbose_name_plural": "Продукты в рецептах",
            },
        ),
    ]