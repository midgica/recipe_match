#take an input unit, convert it to grams, and convert it to output unit
#inputs are strings, function will look up their db entries


from .models import Food, Unit, Ingredient
from decimal import Decimal
from .convert_fractions import convert_fractions


def convert_more_units(food, amount, units, convert_to):


    try:
        food = Food.objects.get(name = food)
    except:
        return "Please select an ingredient."

    try:
        amount = Decimal(amount)
    except:
        return "Please enter a number."
    
    try:
        units = Unit.objects.get(abbr = units)
    except:
        return "Please select a unit to convert from."

    try:
        convert_to = Unit.objects.get(abbr = convert_to)
    except:
        return "Please select a unit to convert to."





    #converting to grams from standard units
        #convert to g first

    #volumetric measurements
    if units.abbr == "fl oz":
        amt_in_c = (amount / Decimal(8))
        amt_in_g = (amt_in_c * food.g_per_c)
    elif units.abbr == "mL":
        amt_in_c = (amount / Decimal(236.6))
        amt_in_g = (amt_in_c * food.g_per_c)
    elif units.abbr == "pinch":
        amt_in_c = (amount / Decimal(384))
        amt_in_g = (amt_in_c * food.g_per_c)
    elif units.abbr == "tbsp":
        amt_in_c = (amount / Decimal(16))
        amt_in_g = (amt_in_c * food.g_per_c)
    elif units.abbr == "tsp":
        amt_in_c = (amount / Decimal(48))
        amt_in_g = (amt_in_c * food.g_per_c)
    elif units.abbr == "c":
        amt_in_c = amount
        amt_in_g = (amt_in_c * food.g_per_c)

    #weight measurements
    elif units.abbr == "g":
        amt_in_g = amount
        amt_in_c = (amt_in_g / food.g_per_c)
    elif units.abbr == "lb":
        amt_in_g = (amount * Decimal(453.6))
        amt_in_c = (amt_in_g / food.g_per_c)
    elif units.abbr == "oz":
        amt_in_g = (amount * Decimal(28.3))
        amt_in_c = (amt_in_g / food.g_per_c)
    
    #nonstandard measurements    
    elif units.abbr == "breast":
        if not food.g_per_breast:
            return "Sorry, this food doesn't have that measurement."
        else:
            amt_in_g = (amount * food.g_per_breast)
            amt_in_c = (amt_in_g / food.g_per_c)
    elif units.abbr == "clove":
        if not food.g_per_clove:
            return "Sorry, this food doesn't have that measurement."
        else:
            amt_in_g = (amount * food.g_per_clove)
            amt_in_c = (amt_in_g / food.g_per_c)
    elif units.abbr == "head":
        if not food.g_per_head:
            return "Sorry, this food doesn't have that measurement."
        else:
            amt_in_g = (amount * food.g_per_head)
            amt_in_c = (amt_in_g / food.g_per_c)
    elif units.abbr == "stalk":
        if not food.g_per_stalk:
            return "Sorry, this food doesn't have that measurement."
        else:
            amt_in_g = (amount * food.g_per_stalk)
            amt_in_c = (amt_in_g / food.g_per_c)
    elif units.abbr == "leaves":
        if not food.g_per_leaf:
            return "Sorry, this food doesn't have that measurement."
        else:
            amt_in_g = (amount * food.g_per_leaf)
            amt_in_c = (amt_in_g / food.g_per_c)
    elif units.abbr == "whole":
        if not food.g_per_whole:
            return "Sorry, this food doesn't have that measurement."
        else:
            amt_in_g = (amount * food.g_per_whole)
            amt_in_c = (amt_in_g / food.g_per_c)
    else:
        return "Unit input error"


    
    #convert to units_out

    #volumetric measurements
    if convert_to.abbr == "c":
        result = amt_in_c
    elif convert_to.abbr == "fl oz":
        result = (amt_in_c * Decimal(8))
    elif convert_to.abbr == "mL":
        result = (amt_in_c * Decimal(236.6))
    elif convert_to.abbr == "pinch":
        result = (amt_in_c * Decimal(384))
    elif convert_to.abbr == "tbsp":
        result = (amt_in_c * Decimal(16))
    elif convert_to.abbr == "tsp":
        result = (amt_in_c * Decimal(48))

    #weight measurements
    elif convert_to.abbr == "g":
        result = amt_in_g
    elif convert_to.abbr == "lb":
        result = (amt_in_g / Decimal(453.6))
    elif convert_to.abbr == "oz":
        result = (amt_in_g / Decimal(28.3))

    #nonstandard measurements
    elif convert_to.abbr == "breast":
        if not food.g_per_breast:
            return "Sorry, this food doesn't have that measurement."
        else:
            result = (amt_in_g / food.g_per_breast)
    elif convert_to.abbr == "clove":
        if not food.g_per_clove:
            return "Sorry, this food doesn't have that measurement."
        else:
            result = (amt_in_g / food.g_per_clove)
    elif convert_to.abbr == "head":
        if not food.g_per_head:
            return "Sorry, this food doesn't have that measurement."
        else:
            result = (amt_in_g / food.g_per_head)
    elif convert_to.abbr == "stalk":
        if not food.g_per_stalk:
            return "Sorry, this food doesn't have that measurement."
        else:
            result = (amt_in_g / food.g_per_stalk)
    elif convert_to.abbr == "leaves":
        if not food.g_per_leaf:
            return "Sorry, this food doesn't have that measurement."
        else:
            result = (amt_in_g / food.g_per_leaf)
    elif convert_to.abbr == "whole":
        if not food.g_per_whole:
            return "Sorry, this food doesn't have that measurement."
        else:
            result = (amt_in_g / food.g_per_whole)
    else:
        return "Unit output error"


    #convert result to friendly fraction
    
    result = convert_fractions(result)
    return result







            
        
