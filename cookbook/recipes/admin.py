from django.contrib import admin

from .models import Product, Recipe, RecipeProduct


class RecipeProductInline(admin.TabularInline):
    """Inline для отображения продуктов в админ-панели рецепта."""

    model = RecipeProduct
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Административная панель для управления рецептами."""

    inlines = (RecipeProductInline,)
    list_display = (
        "id",
        "name",
    )
    list_display_links = ("name",)
    search_fields = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Административная панель для управления продуктами."""

    list_display = (
        "id",
        "name",
        "times_used",
    )
    readonly_fields = ("times_used",)
    list_display_links = ("name",)
    search_fields = ("name",)