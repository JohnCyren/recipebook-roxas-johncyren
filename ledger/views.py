from django.shortcuts import render, HttpResponse
from .models import Recipe, Ingredient

# Create your views here.
def index(request):
    return HttpResponse("")

def recipe_list(request):
    recipe = Recipe.objects.all()
    return render(request, 'ledger/recipe_list.html', {'recipe': recipe})

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'ledger/recipe_detail.html', {'recipe': recipe})
def  ingredient_detail(request, ingredient_id):
    ingredient = Ingredient.objects.get(id=ingredient_id)
    return render(request, 'ledger/ingredient_detail.html', {'ingredient': ingredient})



