from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from .models import Director
# Create your views here.
def homepage(request):
    context ={
        'Movie': Movie.objects.all(),
        'value': 'Filmy'
    }
    return render(request,'main.html',context)

def directors(request):
    context ={
        'Director': Director.objects.all(),
        'value': 'Rezišeři',
    }
    return render(request,'directors.html',context)

def film(request):
    nameReq = request.GET.get('name', '')
    movie = Movie.objects.filter(name=nameReq)
    context ={
        'film': movie,
    }
    return render(request,'film.html',context)