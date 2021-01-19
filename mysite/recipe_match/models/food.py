from django.db import models
from .unit import Unit


class Food(models.Model):
    name = models.CharField(max_length=50)
    plural = models.CharField(max_length=50)

    #units info
    g_per_oz = models.PositiveSmallIntegerField(default=28)
    g_per_c = models.PositiveSmallIntegerField(default=160)
    g_per_in = models.PositiveSmallIntegerField(blank = True, null = True)
    g_per_breast = models.PositiveSmallIntegerField(blank = True, null = True)
    g_per_clove = models.PositiveSmallIntegerField(blank = True, null = True)
    g_per_head = models.PositiveSmallIntegerField(blank = True, null = True)
    g_per_stalk = models.PositiveSmallIntegerField(blank = True, null = True)
    g_per_slice = models.PositiveSmallIntegerField(blank = True, null = True)
    g_per_whole = models.PositiveSmallIntegerField(blank = True, null = True)
    shopping_list_unit = models.ForeignKey(Unit, on_delete=models.CASCADE,
                                           blank=True, null=True)
    
    #nutrition info
    nutrition_link = models.CharField(max_length=200, blank=True)
    calories_in_100g = models.PositiveSmallIntegerField(default=0)
    fat = models.CharField(max_length=10, blank=True) #g
    saturated_fat = models.CharField(max_length=10, blank=True) #g
    trans_fat = models.CharField(max_length=10, blank=True) #g
    cholesterol = models.CharField(max_length=10, blank=True) #mg
    sodium = models.CharField(max_length=10, blank=True) #mg
    total_carbohydrate = models.CharField(max_length=10, blank=True) #g
    dietary_fiber = models.CharField(max_length=10, blank=True) #g
    total_sugars = models.CharField(max_length=10, blank=True) #g
    protein = models.CharField(max_length=10, blank=True) #g

    vit_c = models.CharField(max_length=10, blank=True) #mg
    vit_d = models.CharField(max_length=10, blank=True) #mcg
    iron = models.CharField(max_length=10, blank=True) #mg
    calcium = models.CharField(max_length=10, blank=True) #mg
    potassium = models.CharField(max_length=10, blank=True) #mg
    phosphorus = models.CharField(max_length=10, blank=True) #mg
    
    magnesium = models.CharField(max_length=10, blank=True) #mg
    zinc = models.CharField(max_length=10, blank=True) #mg
    vit_a = models.CharField(max_length=10, blank=True) #mcg
    vit_b = models.CharField(max_length=10, blank=True) #mcg
    vit_e = models.CharField(max_length=10, blank=True) #mg
    vit_k = models.CharField(max_length=10, blank=True) #mcg

    
    def __str__(self):
        return self.name
