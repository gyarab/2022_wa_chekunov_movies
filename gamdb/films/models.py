# Create your models here.
from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.CharField(max_length=1000)
    
    
    def __str__(self):
        return f"{self.name} ({self.year})"

class Anime(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    country = models.CharField(max_length=200)
    raiting = models.IntegerField()
    sfw = models.BooleanField()
    weebStatus = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    