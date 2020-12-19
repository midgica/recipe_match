from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=6, decimal_places=4)
    unit = models.CharField(max_length=20, blank=True)
    notes = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        if not self.unit:
            if self.notes:
                return "%s %s, %s" % (self.amount, self.name, self.notes)
            else:
                return "%s %s" % (self.amount, self.name)
        else:
            if self.notes:
                return "%s %s %s, %s" % (self.amount, self.unit, self.name, self.notes)
            else:
                return "%s %s %s" % (self.amount, self.unit, self.name)
     
