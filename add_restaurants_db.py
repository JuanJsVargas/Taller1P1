import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurantreviews.settings')
django.setup()

from restaurant.models import Restaurant, MenuItem

def add_sample_restaurants():
    # Clear existing data
    Restaurant.objects.all().delete()
    MenuItem.objects.all().delete()

    # Sample Restaurant 1: Italian Restaurant
    italian_restaurant = Restaurant.objects.create(
        name="La Bella Italia",
        description="Authentic Italian cuisine in a cozy atmosphere. Our restaurant brings the flavors of Italy to your table with fresh ingredients and traditional recipes.",
        image="restaurant/images/italian.jpg",
        address="123 Main Street",
        city="New York",
        phone="(555) 123-4567",
        opening_hours="Mon-Sun: 11:00 AM - 10:00 PM",
        cuisine_type="Italian",
        rating=4.8
    )

    # Menu items for Italian Restaurant
    MenuItem.objects.create(
        name="Margherita Pizza",
        description="Fresh tomatoes, mozzarella, basil, and extra virgin olive oil",
        price=14.99,
        category="Pizza",
        restaurant=italian_restaurant
    )
    MenuItem.objects.create(
        name="Spaghetti Carbonara",
        description="Pasta with eggs, cheese, pancetta, and black pepper",
        price=16.99,
        category="Pasta",
        restaurant=italian_restaurant
    )
    MenuItem.objects.create(
        name="Tiramisu",
        description="Classic Italian dessert with coffee-soaked ladyfingers and mascarpone cream",
        price=8.99,
        category="Desserts",
        restaurant=italian_restaurant
    )

    # Sample Restaurant 2: Japanese Restaurant
    japanese_restaurant = Restaurant.objects.create(
        name="Sushi Master",
        description="Experience authentic Japanese cuisine with our fresh sushi and sashimi. We use the finest ingredients and traditional techniques.",
        image="restaurant/images/japanese.jpg",
        address="456 Oak Avenue",
        city="Los Angeles",
        phone="(555) 987-6543",
        opening_hours="Mon-Sun: 12:00 PM - 11:00 PM",
        cuisine_type="Japanese",
        rating=4.9
    )

    # Menu items for Japanese Restaurant
    MenuItem.objects.create(
        name="California Roll",
        description="Crab meat, avocado, cucumber wrapped in rice and seaweed",
        price=12.99,
        category="Sushi Rolls",
        restaurant=japanese_restaurant
    )
    MenuItem.objects.create(
        name="Miso Soup",
        description="Traditional Japanese soup with tofu and seaweed",
        price=4.99,
        category="Soups",
        restaurant=japanese_restaurant
    )
    MenuItem.objects.create(
        name="Tempura Udon",
        description="Hot udon noodles in broth with tempura shrimp",
        price=15.99,
        category="Noodles",
        restaurant=japanese_restaurant
    )

    # Sample Restaurant 3: Mexican Restaurant
    mexican_restaurant = Restaurant.objects.create(
        name="El Sabroso",
        description="Vibrant Mexican cuisine with authentic flavors and spices. Enjoy our homemade tortillas and fresh ingredients.",
        image="restaurant/images/mexican.jpg",
        address="789 Pine Street",
        city="Chicago",
        phone="(555) 456-7890",
        opening_hours="Mon-Sun: 10:00 AM - 9:00 PM",
        cuisine_type="Mexican",
        rating=4.7
    )

    # Menu items for Mexican Restaurant
    MenuItem.objects.create(
        name="Tacos al Pastor",
        description="Marinated pork tacos with pineapple and onions",
        price=12.99,
        category="Tacos",
        restaurant=mexican_restaurant
    )
    MenuItem.objects.create(
        name="Guacamole",
        description="Fresh avocado dip with tomatoes, onions, and cilantro",
        price=8.99,
        category="Appetizers",
        restaurant=mexican_restaurant
    )
    MenuItem.objects.create(
        name="Churros",
        description="Crispy fried dough with cinnamon sugar and chocolate sauce",
        price=6.99,
        category="Desserts",
        restaurant=mexican_restaurant
    )

    print("Sample restaurants and menu items have been added to the database!")

if __name__ == "__main__":
    add_sample_restaurants() 