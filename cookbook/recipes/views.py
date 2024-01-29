from django.db.models import F
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render

from .models import Product, Recipe, RecipeProduct


def add_product_to_recipe(request):
    """Добавляет продукт к рецепту или обновляет его вес."""
    recipe_id = request.GET.get("recipe_id")
    product_id = request.GET.get("product_id")
    weight = request.GET.get("weight")

    if not all([recipe_id, product_id, weight]):
        return HttpResponseBadRequest("Недостаточно параметров")

    try:
        weight = int(weight)
    except ValueError:
        return HttpResponseBadRequest("Некорректный формат веса")

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    product = get_object_or_404(Product, pk=product_id)

    recipe_product = RecipeProduct.objects.filter(
        recipe=recipe, product=product
    ).first()

    if recipe_product:
        recipe_product.weight = weight
        recipe_product.save()
        action = "обновлен в рецепте"
    else:
        recipe_product = RecipeProduct.objects.create(
            recipe=recipe, product=product, weight=weight
        )
        action = "добавлен в рецепт"

    return HttpResponse(f"Продукт '{product.name}' {action} '{recipe.name}'")


def cook_recipe(request):
    """Готовит рецепт, увеличивая счетчик использования продуктов."""
    recipe_id = request.GET.get("recipe_id")

    if not recipe_id:
        return HttpResponseBadRequest("Недостаточно параметров")

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.products.all().update(times_used=F("times_used") + 1)

    return HttpResponse(f"Рецепт '{recipe.name}' приготовлен")


def show_recipes_without_product(request):
    """ "Отображает рецепты, где продукт отсутствует или его вес менее 10 г."""
    product_id = request.GET.get("product_id")

    if not product_id:
        return HttpResponseBadRequest("Недостаточно параметров")

    product = get_object_or_404(Product, pk=product_id)

    recipes = Recipe.objects.exclude(
        recipeproduct__product=product, recipeproduct__weight__gte=10
    )

    context = {"recipes": recipes, "product": product}
    return render(request, "recipes.html", context)
