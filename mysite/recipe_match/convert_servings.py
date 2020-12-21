from .convert_units import convert_units
from .models import Ingredient

def convert_servings(recipe, desired_servings):

    #get how many servings the recipe is currently for
    current_servings = recipe.servings

    #get how many servings the user wants it to be
    #divide one by the other
    coefficient = (desired_servings / current_servings)

    #for every ingredient, create a new ingredient with multiplied amount
    ingredient_list = recipe.ingredient_list.all()
    new_ingredient_list = []
    for ing in ingredient_list:
        amount = (float(ing.amount) * float(coefficient))
        new_ingredient = Ingredient(food = ing.food,
                                    amount = amount,
                                    unit = ing.unit,
                                    notes = ing.notes)
        converted_ingredient = convert_units(new_ingredient)
        
        new_ingredient_list.append(converted_ingredient)

    return new_ingredient_list
    #print this instead of recipe.ingredient_list

