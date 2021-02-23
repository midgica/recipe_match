from .models import Ingredient, Recipe


def remove_orphan_ingredients():

    #make a list of all the ingredients that exist
    all_ingredients = Ingredient.objects.all()

    #make a list of all the ingredients that are actually used
    recipe_ingredients = []
    all_recipes = Recipe.objects.all()
    for each in all_recipes:
        for ing in each.ingredient_list.all():
            recipe_ingredients.append(ing)

    #make a list of orphan ingredients
    orphan_ingredients = []
    for ing in all_ingredients:
        if ing in recipe_ingredients:
            None
        else:
            orphan_ingredients.append(ing)


    print(orphan_ingredients)

    #delete leftover ingredients
    for each in orphan_ingredients:
        each.delete()
