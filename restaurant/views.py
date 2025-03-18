from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64
from .models import Restaurant, MenuItem
from .forms import RestaurantForm, MenuItemForm
from django.views.decorators.http import require_POST

# Create your views here.

def home(request):
    search_term = request.GET.get('searchRestaurant')
    if search_term:
        restaurants = Restaurant.objects.filter(name__icontains=search_term)
    else:
        restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'searchTerm': search_term, 'restaurants': restaurants})

def about(request):
    return render(request, 'about.html')

def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    menu_items = restaurant.menu_items.all()
    return render(request, 'restaurant_detail.html', {
        'restaurant': restaurant,
        'menu_items': menu_items
    })

def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save()
            return redirect('restaurant_detail', restaurant_id=restaurant.id)
    else:
        form = RestaurantForm()
    return render(request, 'add_restaurant.html', {'form': form})

def add_menu_item(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.restaurant = restaurant
            menu_item.save()
            return redirect('restaurant_detail', restaurant_id=restaurant_id)
    else:
        form = MenuItemForm()
    return render(request, 'add_menu_item.html', {'form': form, 'restaurant': restaurant})

def statistics_view(request):
    matplotlib.use('Agg')

    # Get restaurants by cuisine type
    cuisine_counts = {}
    restaurants = Restaurant.objects.values_list('cuisine_type', flat=True)
    
    for cuisine in restaurants:
        if cuisine:
            if cuisine in cuisine_counts:
                cuisine_counts[cuisine] += 1
            else:
                cuisine_counts[cuisine] = 1

    # Get restaurants by city
    city_counts = {}
    restaurants = Restaurant.objects.values_list('city', flat=True)
    
    for city in restaurants:
        if city:
            if city in city_counts:
                city_counts[city] += 1
            else:
                city_counts[city] = 1

    # Create charts
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

    # Generate base64 images
    graphic_cuisine = generate_chart(cuisine_counts, 'Restaurants by Cuisine Type', 'Cuisine Type', 'Number of restaurants')
    graphic_city = generate_chart(city_counts, 'Restaurants by City', 'City', 'Number of restaurants')

    return render(request, 'statistics.html', {
        'graphic_cuisine': graphic_cuisine,
        'graphic_city': graphic_city
    })

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})

@require_POST
def delete_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    restaurant.delete()
    return JsonResponse({'status': 'success'})

