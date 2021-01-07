from django.test import TestCase
from .models import Recipe, Selection, Menu


class Make_Shopping_List_Tests(TestCase):


    def test_make_shopping_list_with_no_repeated_ingredients(self):
        recipe1 = Recipe.objects.get(name = "Moo Shu Pork Tacos")
        recipe2 = Recipe.objects.get(name = "Cream Cheese Pancakes")
        my_menu = Menu.objects.create()
        selection1 = Selection.objects.create(menu = my_menu,
                                              recipe = recipe1,
                                              desired_servings = 8)
        selection2 = Selection.objects.create(menu = my_menu,
                                              recipe = recipe2,
                                              desired_servings = 8)
        shopping_list = make_shopping_list(menu)        
        #this should return a shopping list with 18 ingredients
        self.assertIs(len(shopping_list), 18)



#make_shopping_list_with_repeated_ingredients

#make_shopping_list_with_duplicate_recipes

#make_shopping_list_with_default_servings

#make_shopping_list_with_desired_servings
