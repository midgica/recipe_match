from .models import Food, Ingredient, Menu, Recipe, Selection, Shopping_List, Unit
from .convert_servings import convert_servings

def make_shopping_list(menu):

    
    #break menu into individual recipes
    selections = menu.selection_set.all()

    #break recipes into individual ingredients
    all_ingredients = {}
    duplicate_ingredients = {}
    for sel in selections:
        #convert ingredients by number of servings
        ingredient_list = convert_servings(sel.recipe, sel.desired_servings)
        for ingred in ingredient_list:
            try:
                #if there's already a value for this ingredient
                if all_ingredients[ingred.food]:
                    #if there's only one tuple there
                    try:
                        len(all_ingredients[ingred.food]) == 2
                        for amt, unit in all_ingredients[ingred.food]:
                            #if units match, add them together
                            if ingred.unit == unit:
                                new_amt = amt + ingred.amount
                                all_ingredients[ingred.food] = (new_amt, unit)
                            #otherwise append more values
                            else:
                                all_ingredients.setdefault(key, [])
                                all_ingredients[ingred.food].append(ingred.amount,
                                                                    ingred.unit)

                    except:  #if there's more than one tuple
                        ing_tuple_list = all_ingredients[ingred.food]
                        for each in ing_tuple_list:
                            (amt, unit) = ing_tuple_list[0]
                            #if ingredient units match, add them together
                            if ingred.unit == unit:
                                new_amt = amt + ingred.amount
                                all_ingredients[ingred.food] = (new_amt, unit)
                                amt = None
                                unit = None
                        #if there weren't any matches in the for loop
                        #append more values. if there were matches, append none
                            else:
                                try:
                                    all_ingredients.setdefault(key, [])
                                    all_ingredients[ingred.food].append(ingred.amount,
                                                                        ingred.unit)
                                except: #if appending none produces error
                                    None
            except:
                all_ingredients[ingred.food] = (ingred.amount, ingred.unit)


    shopping_list = []
    for ingred in all_ingredients.keys():            
        for tup in all_ingredients[ingred]:
            tup = all_ingredients[ingred]
            unit = None
            try:
                (amt, unit) = tup
            except ValueError:
                (amt) = tup
        shopping_list.append(Ingredient.objects.create(food = ingred,
                                                       amount = amt,
                                                       unit = unit))


    return shopping_list





### currently returns same shopping_list for multiple recipes as one recipe
### currently does not account for desired_servings
