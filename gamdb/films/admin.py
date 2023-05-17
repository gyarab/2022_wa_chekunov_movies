from django.contrib import admin

from .models import Actor, Anime, Director, Genre, Movie
from .templatetags import random_numbers

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','director','name','year']


class AnimeAdmin(admin.ModelAdmin):
    list_display = ['id','name','year',"country"]

class DirectorAdmin(admin.ModelAdmin):
    list_display = ['id','name','birth_year']

admin.site.register(Movie,MovieAdmin)
admin.site.register(Anime, AnimeAdmin)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Actor)

