from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
# def home_view(request):
#     return HttpResponse('<h1>Welcome to Home Page</h1>')

def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = (
            Movie.objects.filter(title__icontains=searchTerm))
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies})

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})
