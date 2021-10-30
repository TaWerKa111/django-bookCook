from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Ingredient, Recipe

# Register your models here.


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'text',
        'cooking_time',
        'type_of_kitchen',
    ]

    search_fields = (
        "name",
        "ingredients",
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]

    search_fields = ['name']

    ordering = ['name']



