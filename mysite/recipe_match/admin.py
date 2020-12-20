from django.contrib import admin
from .models import Recipe, Ingredient, Category
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.





class IngredientResource(resources.ModelResource):

    class Meta:
        model = Ingredient


class IngredientAdmin(ImportExportModelAdmin):
    resource_class = IngredientResource
        

class RecipeResource(resources.ModelResource):
    
    class Meta:
        model = Recipe
        exclude = ('category',)


class RecipeAdmin(ImportExportModelAdmin):
    resource_class = RecipeResource

#admin.site.register(Recipe)
#admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
