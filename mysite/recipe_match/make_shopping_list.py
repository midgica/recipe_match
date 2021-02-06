from .models import Food, Ingredient, Menu, Recipe, Selection, Shopping_List, Unit
from .convert_servings import convert_servings
from .convert_more_units import convert_more_units
from .unconvert_fractions import unconvert_fractions

def make_shopping_list(menu):

    
    #break menu into individual recipes
    selections = menu.selection_set.all()

    #break recipes into individual ingredients
    all_ingredients = {}
    for sel in selections:
        #convert ingredients by number of servings
        ingredient_list = convert_servings(sel.recipe, sel.desired_servings)
        print(ingredient_list) #debug
        for ingred in ingredient_list:
            #convert to g
            #if unit is not selected
            if ingred.unit == None:
                ingred_grams_str = convert_more_units(food = ingred.food,
                                                      amount = ingred.amount,
                                                      units = 'whole',
                                                      convert_to = 'g')
            else:
                ingred_grams_str = convert_more_units(food = ingred.food,
                                                      amount = ingred.amount,
                                                      units = ingred.unit,
                                                      convert_to = 'g')
            ingred_grams = unconvert_fractions(ingred_grams_str)
            print(ingred.food, ingred_grams, ingred.food.shopping_list_unit) #debug
            test_ingred = Ingredient.objects.create(food = ingred.food,
                                                    amount = ingred_grams,
                                                    unit = ingred.food.shopping_list_unit)
            #if there's already a value for this ingredient
            try:
                old_value = all_ingredients[ingred.food]
                new_value = (all_ingredients[ingred.food] + ingred_grams)
                all_ingredients[ingred.food] = new_value
            #if no values yet
            except:
                all_ingredients[ingred.food] = ingred_grams
                  
    #now we have a dict of food names to gram amounts

    #create empty shopping list
    shopping_list = []

    #work with each ingredient
    for food in all_ingredients.keys():
        #convert to preferred shopping list unit
        #if unit isn't picked, convert to "whole"
        if food.shopping_list_unit == None:
            str_value = convert_more_units(food,
                                           all_ingredients[food],
                                           'g', 'whole')
            final_value = unconvert_fractions(str_value)
            shopping_list.append(Ingredient.objects.create(food = food,
                                                           amount = final_value))
        #if unit is "whole", create ingredient without unit
        elif food.shopping_list_unit.abbr == 'whole':
            str_value = convert_more_units(food,
                                           all_ingredients[food],
                                           'g', 'whole')
            final_value = unconvert_fractions(str_value)
            shopping_list.append(Ingredient.objects.create(food = food,
                                                           amount = final_value))
        #otherwise use unit as entered
        else:
            str_value = convert_more_units(food,
                                           all_ingredients[food],
                                           'g', food.shopping_list_unit.abbr)
            print("str_value =", str_value, " ing =", food.name) #debug
            final_value = unconvert_fractions(str_value)
            shopping_list.append(Ingredient.objects.create(food = food,
                                                           amount = final_value,
                                                           unit = food.shopping_list_unit))
            


    return shopping_list





### currently returns same shopping_list for multiple recipes as one recipe
