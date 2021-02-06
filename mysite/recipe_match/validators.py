from django.core.exceptions import ValidationError
from .models import Food, Ingredient, Unit


def validate_unit_on_food():

    
    #check every ingredient in the db
    for ing in Ingredient.objects.all():
        
        #does food have gram measurement for this unit?
        food = ing.food
        unit = ing.unit

        volumetric_units = ['c', 'fl oz', 'mL', 'pinch', 'tbsp', 'tsp']
        weight_units = ['g', 'lb', 'oz']
        nonstandard_units = ['breast', 'clove', 'head', 'slice', 'stalk',
                             'whole']


        if not unit:
            None

        elif unit.abbr in volumetric_units:
            if food.g_per_c == None:
                msg = ("no msmt for grams per cup of " + str(food.name))
                raise Exception(msg)
            
        elif unit.abbr in weight_units:
            if food.g_per_oz == None:
                msg = ("no msmt for grams per ounce of " + str(food.name))
                raise Exception(msg)            

        elif unit.abbr in nonstandard_units:
            if unit.abbr == 'breast':
                if food.g_per_breast == None:
                    msg = ("no msmt for grams per breast of " + str(food.name))
                    raise Exception(msg)
            elif unit.abbr == 'clove':
                if food.g_per_clove == None:
                    msg = ("no msmt for grams per clove of " + str(food.name))
                    raise Exception(msg)
            elif unit.abbr == 'head':
                if food.g_per_head == None:
                    msg = ("no msmt for grams per head of " + str(food.name))
                    raise Exception(msg)
            elif unit.abbr == 'slice':
                if food.g_per_slice == None:
                    msg = ("no msmt for grams per slice of " + str(food.name))
                    raise Exception(msg)
            elif unit.abbr == 'stalk':
                if food.g_per_stalk == None:
                    msg = ("no msmt for grams per stalk of " + str(food.name))
                    raise Exception(msg)
            elif unit.abbr == 'whole':
                if food.g_per_whole == None:
                    msg = ("no msmt for grams per whole of " + str(food.name))
                    raise Exception(msg)
            else:
                raise Exception("unit not defined in validator")
                    

        else:
            raise Exception("unit not found in validate_unit_on_food")
            


def validate_shopping_list_unit():

    for food in Food.objects.all():
        if shopping_list_unit == None:
            msg = ("no shopping list unit for " + food.name)
            raise Exception(msg)
