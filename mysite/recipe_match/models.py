from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, default='dinner')
    tags = models.CharField(max_length=200, blank=True)
    rating = models.PositiveSmallIntegerField(default=5,
                                              validators=[MaxValueValidator(10),
                                                          MinValueValidator(0)])
    
    amt1 = models.CharField(max_length=10)
    unit1 = models.CharField(max_length=20)
    ingred1 = models.CharField(max_length=100)
    notes1 = models.CharField(max_length=100, blank=True)
    amt2 = models.CharField(max_length=10)
    unit2 = models.CharField(max_length=20)
    ingred2 = models.CharField(max_length=100)
    notes2 = models.CharField(max_length=100, blank=True)
    amt3 = models.CharField(max_length=10)
    unit3 = models.CharField(max_length=20)
    ingred3 = models.CharField(max_length=100)
    notes3 = models.CharField(max_length=100, blank=True)
    amt4 = models.CharField(max_length=10, blank=True)
    unit4 = models.CharField(max_length=20, blank=True)
    ingred4 = models.CharField(max_length=100, blank=True)
    notes4 = models.CharField(max_length=100, blank=True)
    amt5 = models.CharField(max_length=10, blank=True)
    unit5 = models.CharField(max_length=20, blank=True)
    ingred5 = models.CharField(max_length=100, blank=True)
    notes5 = models.CharField(max_length=100, blank=True)
    amt6 = models.CharField(max_length=10, blank=True)
    unit6 = models.CharField(max_length=20, blank=True)
    ingred6 = models.CharField(max_length=100, blank=True)
    notes6 = models.CharField(max_length=100, blank=True)
    amt7 = models.CharField(max_length=10, blank=True)
    unit7 = models.CharField(max_length=20, blank=True)
    ingred7 = models.CharField(max_length=100, blank=True)
    notes7 = models.CharField(max_length=100, blank=True)
    amt8 = models.CharField(max_length=10, blank=True)
    unit8 = models.CharField(max_length=20, blank=True)
    ingred8 = models.CharField(max_length=100, blank=True)
    notes8 = models.CharField(max_length=100, blank=True)
    amt9 = models.CharField(max_length=10, blank=True)
    unit9 = models.CharField(max_length=20, blank=True)
    ingred9 = models.CharField(max_length=100, blank=True)
    notes9 = models.CharField(max_length=100, blank=True)
    amt10 = models.CharField(max_length=10, blank=True)
    unit10 = models.CharField(max_length=20, blank=True)
    ingred10 = models.CharField(max_length=100, blank=True)
    notes10 = models.CharField(max_length=100, blank=True)
    amt11 = models.CharField(max_length=10, blank=True)
    unit11 = models.CharField(max_length=20, blank=True)
    ingred11 = models.CharField(max_length=100, blank=True)
    notes11 = models.CharField(max_length=100, blank=True)
    amt12 = models.CharField(max_length=10, blank=True)
    unit12 = models.CharField(max_length=20, blank=True)
    ingred12 = models.CharField(max_length=100, blank=True)
    notes12 = models.CharField(max_length=100, blank=True)
    amt13 = models.CharField(max_length=10, blank=True)
    unit13 = models.CharField(max_length=20, blank=True)
    ingred13 = models.CharField(max_length=100, blank=True)
    notes13 = models.CharField(max_length=100, blank=True)
    amt14 = models.CharField(max_length=10, blank=True)
    unit14 = models.CharField(max_length=20, blank=True)
    ingred14 = models.CharField(max_length=100, blank=True)
    notes14 = models.CharField(max_length=100, blank=True)
    amt15 = models.CharField(max_length=10, blank=True)
    unit15 = models.CharField(max_length=20, blank=True)
    ingred15 = models.CharField(max_length=100, blank=True)
    notes15 = models.CharField(max_length=100, blank=True)
    amt16 = models.CharField(max_length=10, blank=True)
    unit16 = models.CharField(max_length=20, blank=True)
    ingred16 = models.CharField(max_length=100, blank=True)
    notes16 = models.CharField(max_length=100, blank=True)
    amt17 = models.CharField(max_length=10, blank=True)
    unit17 = models.CharField(max_length=20, blank=True)
    ingred17 = models.CharField(max_length=100, blank=True)
    notes17 = models.CharField(max_length=100, blank=True)
    amt18 = models.CharField(max_length=10, blank=True)
    unit18 = models.CharField(max_length=20, blank=True)
    ingred18 = models.CharField(max_length=100, blank=True)
    notes18 = models.CharField(max_length=100, blank=True)
    amt19 = models.CharField(max_length=10, blank=True)
    unit19 = models.CharField(max_length=20, blank=True)
    ingred19 = models.CharField(max_length=100, blank=True)
    notes19 = models.CharField(max_length=100, blank=True)
    amt20 = models.CharField(max_length=10, blank=True)
    unit20 = models.CharField(max_length=20, blank=True)
    ingred20 = models.CharField(max_length=100, blank=True)
    notes20 = models.CharField(max_length=100, blank=True)

    instructions = models.TextField(max_length=5000)
    
    def __str__(self):
        return self.name