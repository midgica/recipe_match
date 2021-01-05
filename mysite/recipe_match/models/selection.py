from django.db import models
from .menu import Menu
from .recipe import Recipe


class Selection(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    desired_servings = models.PositiveSmallIntegerField(default=8)

    def __str__(self):
        name = self.recipe.name
        servings = self.desired_servings
        return f"{name}, {servings} servings"
