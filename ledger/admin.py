from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile, RecipeImage


# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = [
        ProfileInline,
    ]


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeImageInline]


admin.site.register(Profile)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
