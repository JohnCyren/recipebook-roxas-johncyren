from django.shortcuts import render, HttpResponse
from .models import Recipe, Ingredient
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return HttpResponse("")


@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})


@login_required
def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, "ledger/recipe_detail.html", {"recipe": recipe})


def ingredient_detail(request, ingredient_id):
    ingredient = Ingredient.objects.get(id=ingredient_id)
    return render(request, "ledger/ingredient_detail.html", {"ingredient": ingredient})
