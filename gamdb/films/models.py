# Create your models here.
from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.CharField(max_length=1000, blank=True)
    director = models.ForeignKey('Director', blank=True, null=True, on_delete=models.SET_NULL)
    genres = models.ManyToManyField('Genre',blank=True,)
    def __str__(self):
        return f"{self.name} ({self.year})"
    def genre_display(self):
        return ", ".join([i.name for i in self.genres.all()])

class Anime(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    country = models.CharField(max_length=200)
    raiting = models.IntegerField()
    sfw = models.BooleanField()
    weebStatus = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    

class Genre(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name}"
    



class Director(models.Model):
    name = models.CharField(max_length=200)
    birth_year = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.birth_year})"
