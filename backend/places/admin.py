from django.contrib.gis import admin
from .models import Category, Place


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Place)
class PlaceAdmin(admin.GISModelAdmin):
    list_display = ['name', 'category', 'address']
    list_filter = ['category']
    search_fields = ['name', 'address']
    readonly_fields = ['id', 'latitude', 'longitude', 'created_at', 'updated_at']
    

    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 12,
            'default_lon': 2.3522,
            'default_lat': 48.8566,
        },
    }