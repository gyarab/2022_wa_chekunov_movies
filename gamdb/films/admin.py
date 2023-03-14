from django.contrib import admin
from .models import Movie
from .models import Anime
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','name','year']

class AnimeAdmin(admin.ModelAdmin):
    list_display = ['id','name','year',"country"]

admin.site.register(Movie,MovieAdmin)
admin.site.register(Anime, AnimeAdmin)