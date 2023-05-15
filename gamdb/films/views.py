from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .forms import CommentForm
from .models import Actor, Director, Genre, Movie, Comment


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

# Reziseri
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

def director(request, id):
    context = {
        "director": Director.objects.get(id=id)
    }
    return render(request, 'director.html', context)

# Filmy
def film(request, id):
    m = Movie.objects.get(id=id)
    f = CommentForm()

    if request.POST:
        f = CommentForm(request.POST)
        if f.is_valid():
            # ulozit do DB
            c = Comment(
                movie=m,
                author=f.cleaned_data.get('author'),
                text=f.cleaned_data.get('text'),
                rating=f.cleaned_data.get('rating'),
            )
            if not c.author:
                c.author = 'Anonym'
            c.save()
            # nastavit prazdny form
            f = CommentForm()

    context = {
        "movie": m,
        "comments": Comment.objects.filter(movie=m).order_by('-created_at'),
        "form": f
    }
    return render(request, 'film.html', context)

def films(request):
    context = {
        "movies": movies_queryset,
        "genres": Genre.objects.all().order_by('name'),
        "genre": genre,
        "search": search,
    }
    return render(request, 'films.html', context)