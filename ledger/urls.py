from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("recipes/list", views.recipe_list, name="recipe_list"),
    path("recipe/<int:recipe_id>/", views.recipe_detail, name="recipe_detail"),
    path(
        "ingredient/<int:ingredient_id>/",
        views.ingredient_detail,
        name="ingredient_detail",
    ),
    path("recipe/add/", views.recipe_add, name="recipe_add"),
    path("recipe/<int:recipe_id>/add_image/", views.recipe_image_add, name="add_image"),
]
