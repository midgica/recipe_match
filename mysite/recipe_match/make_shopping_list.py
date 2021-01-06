from .models import Food, Ingredient, Menu, Recipe, Selection, Shopping_List, Unit


def make_shopping_list(menu):

    
    #break menu into individual recipes
    selections = menu.selection_set.all()

    #break recipes into individual ingredients
    all_ingredients = {}
    duplicate_ingredients = {}
    for each in selections:
        for ingred in Ingredient.objects.filter(recipe = each.recipe):
            try:
                if all_ingredients[ingred.food]:
                    ing_tuple = all_ingredients[ingred.food]
                    for amt, unit in ing_tuple:
                        #if ingredient units match, add them together 
                        if ingred.unit == unit:
                            new_amt = amt + ingred.amount
                            all_ingredients[ingred.food] = (new_amt, unit)
                        #otherwise append more values
                        else:
                            all_ingredients.setdefault(key, [])
                            all_ingredients[ingred.food].append(ingred.amount,
                                                                ingred.unit)
            except:
                all_ingredients[ingred.food] = (ingred.amount, ingred.unit)


    shopping_list = []
    for ingred in all_ingredients.keys():            
        for tup in all_ingredients[ingred]:
            tup = all_ingredients[ingred]
            unit = None
            try:
                (amt, unit) = tup
                print(amt)
                print(unit)
            except ValueError:
                (amt) = tup
        shopping_list.append(Ingredient.objects.create(food = ingred,
                                                       amount = amt,
                                                       unit = unit))


    return shopping_list





### currently returns same shopping_list for multiple recipes as one recipe
### currently does not account for desired_servings
