from django.contrib import admin
from django.utils.html import format_html
from .models import Restaurant, MenuItem

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    fields = ['name', 'description', 'price', 'category', 'image']
    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px;"/>', obj.image.url)
        return "No image"

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'cuisine_type', 'rating', 'phone', 'preview_image']
    list_filter = ['city', 'cuisine_type']
    search_fields = ['name', 'description', 'address', 'city']
    ordering = ['name']
    inlines = [MenuItemInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'image')
        }),
        ('Location & Contact', {
            'fields': ('address', 'city', 'phone')
        }),
        ('Restaurant Details', {
            'fields': ('cuisine_type', 'opening_hours', 'rating')
        }),
    )

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px;"/>', obj.image.url)
        return "No image"
    preview_image.short_description = 'Image'

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'restaurant', 'price', 'category', 'preview_image']
    list_filter = ['category', 'restaurant']
    search_fields = ['name', 'description', 'restaurant__name']
    ordering = ['restaurant', 'category', 'name']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'price')
        }),
        ('Classification', {
            'fields': ('category', 'restaurant')
        }),
        ('Image', {
            'fields': ('image',)
        }),
    )

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px;"/>', obj.image.url)
        return "No image"
    preview_image.short_description = 'Image'