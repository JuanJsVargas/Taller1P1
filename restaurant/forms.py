from django import forms
from .models import Restaurant, MenuItem

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'image', 'address', 'city', 'phone', 'opening_hours', 'cuisine_type', 'rating']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'opening_hours': forms.TextInput(attrs={'placeholder': 'e.g., Mon-Sun: 11:00 AM - 10:00 PM'}),
        }

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'price': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        } 