from django.db import models
import fractions


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=6, decimal_places=4)
    unit = models.CharField(max_length=20, blank=True)
    notes = models.CharField(max_length=100, blank=True)
    
    def __str__(self):

        if int(self.amount) == self.amount:
            self.amt_str = int(self.amount)
        else: ##convert to fraction
            if self.amount < 1:
                frac = fractions.Fraction(self.amount).limit_denominator(12)
                #print somehow
                self.amt_str = str(frac)
            else:  ## if not < 1 then a mixed fraction is needed
                whole = int(self.amount)
                portion = self.amount - whole
                frac = fractions.Fraction(portion).limit_denominator(12)
                ## display whole next to converted frac
                self.amt_str = (str(whole) + " " + str(frac))
        
        
        if not self.unit:
            if self.notes:
                return "%s %s, %s" % (self.amt_str, self.name, self.notes)
            else:
                return "%s %s" % (self.amt_str, self.name)
        else:
            if self.notes:
                return "%s %s %s, %s" % (self.amt_str, self.unit, self.name, self.notes)
            else:
                return "%s %s %s" % (self.amt_str, self.unit, self.name)
     
