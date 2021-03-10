from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .ingredient import Ingredient
from .category import Category


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.CharField(max_length=200, blank=True)
    servings = models.PositiveSmallIntegerField(default=4,
                                                validators=[MinValueValidator(1)])
    rating = models.PositiveSmallIntegerField(default=5,
                                              validators=[MaxValueValidator(10),
                                                          MinValueValidator(0)])
    ingredient_list = models.ManyToManyField(Ingredient)
                                             #limit_choices_to={'amount': 7})
    instructions = models.TextField(max_length=5000)
    source = models.CharField(max_length=1000, blank=True)
    
    def __str__(self):
        return self.name
