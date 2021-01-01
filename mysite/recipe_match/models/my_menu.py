from django.db import models
from .recipe import Recipe


class My_Menu(models.Model):

    name = models.CharField(max_length=100, blank=True) #if user wants name
    notes = models.TextField(max_length=2000, blank=True) #if user wants notes
    recipe_list = models.ManyToManyField(Recipe) #can i append/delete from this
# how does a user save and retrieve
