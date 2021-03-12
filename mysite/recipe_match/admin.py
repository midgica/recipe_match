from django.contrib import admin
from django import forms
from .models import Food, Unit, Ingredient, Category, Recipe, Menu
from .models import Shopping_List, Selection
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class FoodResource(resources.ModelResource):
    class Meta:
        model = Food
class FoodAdmin(ImportExportModelAdmin):
    resource_class = FoodResource
    list_display = ('name', 'plural')

class UnitResource(resources.ModelResource):
    class Meta:
        model = Unit
class UnitAdmin(ImportExportModelAdmin):
    resource_class = UnitResource
    list_display = ('abbr', 'full')

class IngredientResource(resources.ModelResource):
    class Meta:
        model = Ingredient
class IngredientAdmin(ImportExportModelAdmin):
    resource_class = IngredientResource
    fields = ['amount', 'unit', 'food', 'notes']
#    list_display = ('food', 'notes')

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource

class RecipeResource(resources.ModelResource):    
    class Meta:
        model = Recipe
class RecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        recent_ingredients = Ingredient.objects.all().order_by('pk').reverse()[:50]
        w = self.fields['ingredient_list'].widget
        choices = []
        for choice in recent_ingredients:
            choices.append((choice.id, choice.__str__))
        w.choices = choices
class RecipeAdmin(ImportExportModelAdmin):
    resource_class = RecipeResource
    filter_horizontal = ('ingredient_list',)
    list_display = ('name', 'category')
    form = RecipeForm

class SelectionInline(admin.TabularInline):
    model = Selection
    extra = 1

class MenuResource(resources.ModelResource):
    class Meta:
        model = Menu
class MenuAdmin(ImportExportModelAdmin):
    resource_class = MenuResource
    inlines = [SelectionInline]

class Shopping_ListResource(resources.ModelResource):
    class Meta:
        model = Shopping_List
class Shopping_ListAdmin(ImportExportModelAdmin):
    resource_class = Shopping_ListResource




admin.site.register(Food, FoodAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Shopping_List, Shopping_ListAdmin)
