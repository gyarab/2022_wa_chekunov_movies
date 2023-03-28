from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.
def homepage(request):
    context ={
        'Movie': Movie.objects.all(),
        'value': 'Filmy'
    }
    return render(request,'main.html',context)