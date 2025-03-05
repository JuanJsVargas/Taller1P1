from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64
from .models import Movie

# Create your views here.

def home(request):
   # return HttpResponse('<h1>Welcome to Home Page</h1>')
   # return render(request, 'home.html')
   # return render(request, 'home.html', {'name':'Juan José Vargas'})
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies': movies})

def about(request):
    return render(request, 'about.html')

def statistics_view(request):
    matplotlib.use('Agg')

    # Obtener años únicos ordenados
    years = Movie.objects.values_list('year', flat=True).distinct().order_by('year')
    
    # Contar películas por año
    movie_counts_by_year = {}
    for year in years:
        if year:
            count = Movie.objects.filter(year=year).count()
        else:
            count = Movie.objects.filter(year__isnull=True).count()
            year = "None"
        movie_counts_by_year[year] = count

    # Obtener géneros y contar solo el primer género de cada película
    movies = Movie.objects.values_list('genre', flat=True)
    genre_counts = {}

    for movie_genres in movies:
        if movie_genres:
            first_genre = movie_genres.split(',')[0].strip()  # Tomar solo el primer género
            if first_genre in genre_counts:
                genre_counts[first_genre] += 1
            else:
                genre_counts[first_genre] = 1

    # Crear gráficos
    def generate_chart(data, title, xlabel, ylabel):
        plt.figure()
        positions = range(len(data))
        plt.bar(positions, data.values(), width=0.5, align='center')
        plt.xticks(positions, data.keys(), rotation=90)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.subplots_adjust(bottom=0.3)
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()
        return base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Generar imágenes base64
    graphic_years = generate_chart(movie_counts_by_year, 'Movies per year', 'Year', 'Number of movies')
    graphic_genre = generate_chart(genre_counts, 'Movies per genre', 'Genre', 'Number of movies')

    return render(request, 'statistics.html', {'graphic_years': graphic_years, 'graphic_genre': graphic_genre})

def signup(request):
    email = request.GET.get('email')

    return render(request, 'signup.html', {'email': email})

