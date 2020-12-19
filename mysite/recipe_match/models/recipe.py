from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .ingredient import Ingredient


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, default='dinner')
    tags = models.CharField(max_length=200, blank=True)
    servings = models.PositiveSmallIntegerField(default=4,
                                                validators=[MinValueValidator(1)])
    rating = models.PositiveSmallIntegerField(default=5,
                                              validators=[MaxValueValidator(10),
                                                          MinValueValidator(0)])
    ingredient_list = models.ManyToManyField(Ingredient)
    instructions = models.TextField(max_length=5000)
    
    def __str__(self):
        return self.name
