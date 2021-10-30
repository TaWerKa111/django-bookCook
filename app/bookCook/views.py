from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.urls import reverse
from .models import Ingredient, Recipe
# Create your views here.


def recipe_detail(request, pk):
    """ Полная информация по рецепту с пошаговой инструкцией """
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.recipe_text = recipe.text.strip().split('\n')
    return render(
        request,
        'bookCook/recipe_detail.html',
        {'recipe': recipe}
    )


def home(request):
    """ Список рецептов с поиском по назвению и ингредиентам"""

    try:
        recipe_id = int(request.GET.get("recipe_id"))
    except (ValueError, TypeError):
        recipe_id = None

    try:
        ingredient_id = int(request.GET.get("ingredient_id"))
    except (ValueError, TypeError):
        ingredient_id = None

    query = Q()
    if recipe_id:
        query.add(
            Q(pk=recipe_id), Q.AND,
        )
    if ingredient_id:
        query.add(
            Q(ingredients__pk=ingredient_id), Q.AND,
        )

    recipes_object = Recipe.objects.prefetch_related("ingredients").filter(query)
    recipes = Recipe.objects.all()
    ingredients = Ingredient.objects.all()


    return render(
        request,
        'bookCook/recipes.html',
        {
        'recipes': recipes_object,
        'form': {
            'description': "Здесь вы можете ввести название рецепта или ингредиента",
            'ingredient': {
                'name': 'Ингредиент',
                'objects': ingredients,
                'selected': ingredient_id,
            },
            'recipe': {
                'name': 'Название',
                'objects': recipes,
                'selected': recipe_id,
            },
        }
        }
        )
