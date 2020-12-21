from django.db import models


class Unit(models.Model):
    abbr = models.CharField(max_length=30)
    plural = models.CharField(max_length=30, blank=True)
    full = models.CharField(max_length=30, blank=True)
    full_plural = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.abbr
    
