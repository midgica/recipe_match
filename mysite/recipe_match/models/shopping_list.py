from django.db import models
from .recipe import Recipe
from .ingredient import Ingredient
from .unit import Unit
from .food import Food
from .my_menu import My_Menu

# make a function to create the shopping list and the model to store it
class Shopping_List(models.Model, my_menu=None):

    name = models.CharField(max_length=100, blank=True) #if user wants name
    notes = models.TextField(max_length=2000, blank=True) #if user wants notes
    menu = my_menu
    ingredients = models.ManyToManyField(Ingredient) #already combined if like
