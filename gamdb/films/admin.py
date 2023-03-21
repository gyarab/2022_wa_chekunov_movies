from django.contrib import admin
from .models import Movie
from .models import Anime
from .models import Director
from .models import Genre
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
