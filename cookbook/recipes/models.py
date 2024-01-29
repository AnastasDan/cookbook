from django.db import models


class Product(models.Model):
    """Модель для представления продуктов."""

    name = models.CharField("Название продукта", max_length=255, unique=True)
    times_used = models.IntegerField(
        "Количество использований продукта", default=0
    )

    class Meta:
        ordering = ("id",)
        verbose_name = "продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Модель для представления рецептов."""

    name = models.CharField("Название рецепта", max_length=255)
    products = models.ManyToManyField(
        Product, through="RecipeProduct", verbose_name="Продукты в рецепте"
    )

    class Meta:
        ordering = ("id",)
        verbose_name = "рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.name


class RecipeProduct(models.Model):
    """Модель для представления продуктов в рецептах."""

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, verbose_name="Рецепт"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Продукт"
    )
    weight = models.IntegerField("Вес продукта в рецепте")

    class Meta:
        ordering = ("id",)
        verbose_name = "продукт в рецепте"
        verbose_name_plural = "Продукты в рецептах"
        unique_together = (("recipe", "product"),)

    def __str__(self):
        return f"{self.product.name} ({self.weight} г)"
