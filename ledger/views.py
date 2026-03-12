from django.shortcuts import render, HttpResponse
from .models import Recipe, Ingredient
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, RecipeImageForm
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return HttpResponse("")


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


@login_required
def recipe_add(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect("recipe_detail", recipe_id=recipe.id)
    else:
        form = RecipeForm()

    return render(request, "ledger/recipe_add.html", {"form": form})


@login_required
def recipe_image_add(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()
            return redirect("recipe_detail", recipe_id=recipe.id)
    else:
        form = RecipeImageForm()

    return render(
        request, "ledger/recipe_image_add.html", {"form": form, "recipe": recipe}
    )
