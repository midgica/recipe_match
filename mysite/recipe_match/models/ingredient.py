from django.db import models
from .food import Food
from .unit import Unit
from recipe_match.convert_fractions import convert_fractions


class Ingredient(models.Model):
    ##name = models.CharField(max_length=100)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    ##unit = models.CharField(max_length=20, blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True)
    
    def __str__(self):

        self.amt_str = convert_fractions(self.amount)

##        if int(self.amount) == self.amount:
##            self.amt_str = int(self.amount)
##        else: ##convert to fraction
##            if self.amount < 1:
##                frac = fractions.Fraction(self.amount).limit_denominator(12)
##                #print somehow
##                self.amt_str = str(frac)
##            else:  ## if not < 1 then a mixed fraction is needed
##                whole = int(self.amount)
##                portion = self.amount - whole
##                frac = fractions.Fraction(portion).limit_denominator(12)
##                ## display whole next to converted frac
##                self.amt_str = (str(whole) + " " + str(frac))
        
        
        if not self.unit:
            if self.notes:
                if self.amount > 1:
                    return "%s %s, %s" % (self.amt_str, self.food.plural, self.notes)
                else:
                    return "%s %s, %s" % (self.amt_str, self.food, self.notes)
            else:
                if self.amount > 1:
                    return "%s %s" % (self.amt_str, self.food.plural)
                else:
                    return "%s %s" % (self.amt_str, self.food)
        else:
            if self.notes:
                if self.amount > 1:
                    return "%s %s %s, %s" % (self.amt_str, self.unit, self.food.plural, self.notes)
                else:          
                    return "%s %s %s, %s" % (self.amt_str, self.unit, self.food, self.notes)
            else:
                if self.amount > 1:
                    return "%s %s %s" % (self.amt_str, self.unit, self.food.plural)
                else:
                    return "%s %s %s" % (self.amt_str, self.unit, self.food)
     
