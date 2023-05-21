from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .forms import CommentForm
from .models import Actor, Comment, Director, Genre, Movie


# Create your views here.
def homepage(request):
    top_filmy = Movie.objects.all().order_by('avg_rating').reverse()
    
    # raiting update 
    
    for m in Movie.objects.all():
        sum = 0        
        for comm in Comment.objects.filter(movie=m):
            if comm.rating != None:
                sum += comm.rating
        if not len(Comment.objects.filter(movie=m)) == 0:
            m.avg_rating = round(sum/len(Comment.objects.filter(movie=m)))
            m.save()
    
    context = { 
        # TODO use first 10 top rated
        "top_movies": top_filmy,
        "top_3": top_filmy[0:3]
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
    context = {
        "director": Director.objects.get(id=id)
    }
    return render(request, 'director.html', context)

# Herci
def actors(request):
    context = {
        "actors": Actor.objects.all()
    }
    return render(request, 'actors.html', context)

def actor(request, id):
    context = {
        "actor": Actor.objects.get(id=id)
    }
    return render(request, 'actor.html', context)
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
            # pocitani ratingu
            sum = 0
            valid_raiting =0
            for comm in Comment.objects.filter(movie=m):
                if comm.rating:
                    sum+=comm.rating
                    valid_raiting +=1
            m.avg_rating = round(sum/valid_raiting)
            m.save()
            # nastavit prazdny form
            f = CommentForm()

    context = {
        "movie": m,
        "comments": Comment.objects.filter(movie=m).order_by('-created_at'),
        "form": f
    }
    return render(request, 'film.html', context)

def films(request):
    movies_queryset = Movie.objects.all()
    genre = request.GET.get('genre')
    if genre:
        movies_queryset = movies_queryset.filter(genres__name=genre)
    search = request.GET.get('search')
    if search:
        movies_queryset = movies_queryset.filter(Q(name__icontains=search)|Q(description__icontains=search))

    context = {
        "movies": movies_queryset,
        "genres": Genre.objects.all().order_by('name'),
        "genre": genre,
        "search": search,
    }
    return render(request, 'films.html', context)