from django.db import transaction
from django.db.models import F
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render

from .models import Product, Recipe, RecipeProduct


@transaction.atomic
def add_product_to_recipe(request):
    """Добавляет продукт к рецепту или обновляет его вес."""
    try:
        recipe_id = request.GET.get("recipe_id")
        product_id = request.GET.get("product_id")
        weight = int(request.GET.get("weight"))
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        product = get_object_or_404(Product, pk=product_id)

        recipe_product, created = RecipeProduct.objects.update_or_create(
            recipe=recipe, product=product, defaults={"weight": weight}
        )

        return HttpResponse(
            f"Продукт '{product.name}' "
            f"{'добавлен в рецепт' if created else 'обновлен в рецепте'} "
            f"'{recipe.name}'"
        )

    except ValueError as ve:
        return HttpResponseBadRequest(f"Некорректный формат: {ve}")

    except Exception as e:
        return HttpResponseBadRequest(f"Ошибка: {e}")


@transaction.atomic
def cook_recipe(request):
    """Готовит рецепт, увеличивая счетчик использования продуктов."""
    try:
        recipe_id = request.GET.get("recipe_id")
        recipe = get_object_or_404(Recipe, pk=recipe_id)

        recipe.products.all().update(times_used=F("times_used") + 1)
        return HttpResponse(f"Рецепт '{recipe.name}' приготовлен")

    except ValueError as ve:
        return HttpResponseBadRequest(f"Некорректный формат: {ve}")

    except Exception as e:
        return HttpResponseBadRequest(f"Ошибка: {e}")


def show_recipes_without_product(request):
    """ "Отображает рецепты, где продукт отсутствует или его вес менее 10 г."""
    try:
        product_id = request.GET.get("product_id")
        product = get_object_or_404(Product, pk=product_id)

        recipes = Recipe.objects.exclude(
            recipeproduct__product=product, recipeproduct__weight__gte=10
        ).distinct()

        context = {"recipes": recipes, "product": product}
        return render(request, "recipes.html", context)

    except ValueError as ve:
        return HttpResponseBadRequest(f"Некорректный формат: {ve}")

    except Exception as e:
        return HttpResponseBadRequest(f"Ошибка: {e}")
