#take an input unit, convert it to grams, and convert it to output unit


from .models import Food, Unit, Ingredient
from decimal import Decimal


def convert_more_units(food, amount, units_in, units_out):

    if units_in == None:
        return None

    try:
        amount = Decimal(amount.strip(''))
    except:
        return "Please enter a number."

    #converting to grams from standard units
        #convert to g first

    #volumetric measurements
    if units_in.abbr == "fl oz":
        amt_in_c = (amount / 8)
        amt_in_g = (amt_in_c * food.g_per_cup)
    elif units_in.abbr == "mL":
        amt_in_c = (amount / 236.6)
        amt_in_g = (amt_in_c * food.g_per_cup)
    elif units_in.abbr == "pinch":
        amt_in_c = (amount / 384)
        amt_in_g = (amt_in_c * food.g_per_cup)
    elif units_in.abbr == "tbsp":
        amt_in_c = (amount / 16)
        amt_in_g = (amt_in_c * food.g_per_cup)
    elif units_in.abbr == "tsp":
        amt_in_c = (amount / 48)
        amt_in_g = (amt_in_c * food.g_per_cup)
    elif units_in.abbr == "c":
        amt_in_c = amount
        amt_in_g = (amt_in_c * food.g_per_cup)

    #weight measurements
    elif units_in.abbr == "g":
        None
    elif units_in.abbr == "lb":
        amt_in_g = (amount * 453.6)
        amt_in_c = (amt_in_g / food.g_per_cup)
    elif units_in.abbr == "oz":
        amt_in_g = (amount * 28.3)
        amt_in_c = (amt_in_g / food.g_per_cup)
    
    #nonstandard measurements    
    elif units_in.abbr == "breast":
        if not food.g_per_breast:
            return "Sorry, this food doesn't have that measurement."
        else:
            amt_in_g = (amount * food.g_per_breast)
            amt_in_c = (amt_in_g / food.g_per_cup)
    elif units_in.abbr == "clove":
        if not food.g_per_clove:
            return "Sorry, this food doesn't have that measurement."
        else:
            amt_in_g = (amount * food.g_per_clove)
            amt_in_c = (amt_in_g / food.g_per_cup)
    elif units_in.abbr == "head":
        if not food.g_per_head:
            return "Sorry, this food doesn't have that measurement."
        else:
            amt_in_g = (amount * food.g_per_head)
            amt_in_c = (amt_in_g / food.g_per_cup)
    elif units_in.abbr == "stalk":
        if not food.g_per_stalk:
            return "Sorry, this food doesn't have that measurement."
        else:
            amt_in_g = (amount * food.g_per_stalk)
            amt_in_c = (amt_in_g / food.g_per_cup)
    elif units_in.abbr == "whole":
        if not food.g_per_whole:
            return "Sorry, this food doesn't have that measurement."
        else:
            amt_in_g = (amount * food.g_per_whole)
            amt_in_c = (amt_in_g / food.g_per_cup)
    else:
        return "Unit input error"


    
    #convert to units_out

    #volumetric measurements
    if units_out.abbr == "c":
        result = amt_in_c
    elif units_out.abbr == "fl oz":
        result = (amt_in_c * 8)
    elif units_out.abbr == "mL":
        result = (amt_in_c * 236.6)
    elif units_out.abbr == "pinch":
        result = (amt_in_c * 384)
    elif units_out.abbr == "tbsp":
        result = (amt_in_c * 16)
    elif units_out.abbr == "tsp":
        result = (amt_in_c * 48)

    #weight measurements
    elif units_out.abbr == "g":
        result = amt_in_g
    elif units_out.abbr == "lb":
        result = (amt_in_g / 453.6)
    elif units_out.abbr == "oz":
        result = (amt_in_g / 28.3)

    #nonstandard measurements
    elif units_out.abbr == "breast":
        if not food.g_per_breast:
            return "Sorry, this food doesn't have that measurement."
        else:
            result = (amt_in_g / food.g_per_breast)
    elif units_out.abbr == "clove":
        if not food.g_per_clove:
            return "Sorry, this food doesn't have that measurement."
        else:
            result = (amt_in_g / food.g_per_clove)
    elif units_out.abbr == "head":
        if not food.g_per_head:
            return "Sorry, this food doesn't have that measurement."
        else:
            result = (amt_in_g / food.g_per_head)
    elif units_out.abbr == "stalk":
        if not food.g_per_stalk:
            return "Sorry, this food doesn't have that measurement."
        else:
            result = (amt_in_g / food.g_per_stalk)
    elif units_out.abbr == "whole":
        if not food.g_per_whole:
            return "Sorry, this food doesn't have that measurement."
        else:
            result = (amt_in_g / food.g_per_whole)
    else:
        return "Unit output error"

    return result







            
        
