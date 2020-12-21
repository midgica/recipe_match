from django.contrib import admin
from .models import Food, Unit, Ingredient, Category, Recipe
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class FoodResource(resources.ModelResource):
    class Meta:
        model = Food
class FoodAdmin(ImportExportModelAdmin):
    resource_class = FoodResource

class UnitResource(resources.ModelResource):
    class Meta:
        model = Unit
class UnitAdmin(ImportExportModelAdmin):
    resource_class = UnitResource

class IngredientResource(resources.ModelResource):
    class Meta:
        model = Ingredient
class IngredientAdmin(ImportExportModelAdmin):
    resource_class = IngredientResource

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource

class RecipeResource(resources.ModelResource):    
    class Meta:
        model = Recipe
class RecipeAdmin(ImportExportModelAdmin):
    resource_class = RecipeResource


admin.site.register(Food, FoodAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
