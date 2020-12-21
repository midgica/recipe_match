#go through each unit. if it's too small, convert it to something smaller.
#if it's too big, convert it to something bigger
#fraction conversion happens in ingredient.py and convert_fractions.py, not here
from .models import Ingredient, Unit

#tsp, tbsp, c
#oz, lb


def convert_units(ingredient):
    if ingredient.unit:
        if ingredient.unit.abbr == "tsp":
            multiply_amt = 1
            new_abbr = "tsp"

            if ingredient.amount < 0.125:
                multiply_amt = 8
                new_abbr = "pinch"
            elif ingredient.amount > 3:
                multiply_amt = (1/3)
                new_abbr = "tbsp"
            else:
                None

            return Ingredient(food = ingredient.food,
                              amount = (ingredient.amount * multiply_amt),
                              unit = Unit.objects.get(abbr = new_abbr),
                              notes = ingredient.notes)
	    # don't forget to print this instead of the old ingredient

        if ingredient.unit.abbr == "tbsp":
            multiply_amt = 1
            new_abbr = "tbsp"

            if ingredient.amount < 1:
                multiply_amt = 3
                new_abbr = "tsp"
            elif ingredient.amount > 4:
                multiply_amt = (1/4)
                new_abbr = "c"
            else:
                None

            return Ingredient(food = ingredient.food,
                              amount = (ingredient.amount * multiply_amt),
                              unit = Unit.objects.get(abbr = new_abbr),
                              notes = ingredient.notes)

        if ingredient.unit.abbr == "c":
            multiply_amt = 1
            new_abbr = "c"

            if ingredient.amount < .25:
                multiply_amt = 16
                new_abbr = "tbsp"
            else:
                None

            return Ingredient(food = ingredient.food,
                              amount = (ingredient.amount * multiply_amt),
                              unit = Unit.objects.get(abbr = new_abbr),
                              notes = ingredient.notes)


        if ingredient.unit.abbr == "oz":
            multiply_amt = 1
            new_abbr = "oz"

            if ingredient.amount > 16:
                multiply_amt = (1/16)
                new_abbr = "lb"
            else:
                None

            return Ingredient(food = ingredient.food,
                              amount = (ingredient.amount * multiply_amt),
                              unit = Unit.objects.get(abbr = new_abbr),
                              notes = ingredient.notes)


        if ingredient.unit.abbr == "lb":
            multiply_amt = 1
            new_abbr = "lb"

            if ingredient.amount < .25:
                multiply_amt = 16
                new_abbr = "oz"
            else:
                None

            return Ingredient(food = ingredient.food,
                              amount = (ingredient.amount * multiply_amt),
                              unit = Unit.objects.get(abbr = new_abbr),
                              notes = ingredient.notes)







        
        else: #if an unlisted unit (not converting)
            return Ingredient(food = ingredient.food,
                              amount = ingredient.amount,
                              unit = ingredient.unit,
                              notes = ingredient.notes)

        
	
    else: #if no unit
        return Ingredient(food = ingredient.food,
                          amount = ingredient.amount,
                          notes = ingredient.notes)
