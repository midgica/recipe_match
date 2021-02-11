from django.test import TestCase
from .models import Recipe, Selection, Menu, Ingredient
import re


class Convert_More_Units_Tests(TestCase):

    def test_convert_more_units_all_ingredients_to_grams(self):
        ingredient_set = Ingredient.objects.all()
        ing_grams_list = []
        for ing in ingredient_set:
            if ing.unit == None:
                ing_grams = convert_more_units(ing.food, ing.amount, 'whole',
                                               'g')
            else:
                ing_grams = convert_more_units(ing.food, ing.amount, ing.unit,
                                               'g')
            ing_grams_list.append(ing_grams)

        for each in ing_grams_list:
            print(each)
            

##class Make_Shopping_List_Tests(TestCase):
##
##
##    def test_make_shopping_list_with_no_repeated_ingredients(self):
##        recipe1 = Recipe.objects.get(name = "Moo Shu Pork Tacos")
##        recipe2 = Recipe.objects.get(name = "Cream Cheese Pancakes")
##        my_menu = Menu.objects.create()
##        selection1 = Selection.objects.create(menu = my_menu,
##                                              recipe = recipe1,
##                                              desired_servings = 8)
##        selection2 = Selection.objects.create(menu = my_menu,
##                                              recipe = recipe2,
##                                              desired_servings = 8)
##        shopping_list = make_shopping_list(menu)        
##        #this should return a shopping list with 18 ingredients
##        self.assertIs(len(shopping_list), 18)
##


#make_shopping_list_with_repeated_ingredients

#make_shopping_list_with_duplicate_recipes

#make_shopping_list_with_default_servings

#make_shopping_list_with_desired_servings
