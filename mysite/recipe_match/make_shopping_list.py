from .models import Food, Ingredient, Menu, Recipe, Selection, Shopping_List, Unit


def make_shopping_list(menu):

    
    #break menu into individual recipes
    selections = menu.selection_set.all()

    #break recipes into individual ingredients
    all_ingredients = {}
    duplicate_ingredients = {}
    for each in selections:
        for ingred in recipe.ingredient_list:
            if not all_ingredients[ingred.food]:
                all_ingredients[ingred.food] = [(ingred.amount, ingred.unit)]
            else:
                ing_tuple = all_ingredients[ingred.food]
                for amt, unit in ing_tuple:
                    #if ingredient units match, add them together 
                    if ingred.unit == unit:
                        new_amt = amt + ingred.amount
                        all_ingredients[ingred.food] = (new_amt, unit)
                    #otherwise append more values
                    else:
                        all_ingredients.setdefault(key, [])
                        all_ingredients[ingred.food].append(ingred.amount, ingred.unit)


    shopping_list = []
    for ingred in all_ingredients.keys():
        food = ingred
        #loop through the values to assemble a readable list
        while (amt, unit) in all_ingredients[ingred]:
            amount = amt
            unit = unit
            shopping_list.append(f"{amt} {unit} {food}")            
            all_ingredients.ingred.remove(amt, unit)


    return shopping_list


