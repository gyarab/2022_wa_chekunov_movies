from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from .models import Director, Genre, Actor
# Create your views here.
def homepage(request):
    context = {
        # TODO use first 10 top rated
        "movies": Movie.objects.all(),
        "actors": Actor.objects.all(),
        "directors": Director.objects.all(),
        "genres": Genre.objects.all(),
    }
    return render(request, 'homepage.html', context)

def directors(request):
    context ={
        'Director': Director.objects.all(),
        'value': 'Rezišeři',
    }
    return render(request,'directors.html',context)
def director(request, id):
    context ={
        'Director': Director.objects.all(),
        'value': 'Rezišeři',
    }
    return render(request,'directors.html',context)

def film(request, id):
    context = {
        "movie": Movie.objects.get(id=id)
    }
    return render(request, 'film.html', context)

def films(request):
    context = {
        "movies": Movie.objects.all()
    }
    return render(request, 'films.html', context)