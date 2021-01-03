from django.db import models
from .recipe import Recipe
from django.contrib.auth.models import User


class Menu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True) #if user wants name
    notes = models.TextField(max_length=2000, blank=True) #if user wants notes
    recipe_dict = {} #key is recipe.id, value is desired_servings
# how does a user save and retrieve
