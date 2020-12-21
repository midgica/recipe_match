from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=50)
    plural = models.CharField(max_length=50)

    def __str__(self):
        return self.name
