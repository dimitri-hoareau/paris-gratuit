from rest_framework import serializers
from .models import Category, Place


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'color', 'icon', 'created_at', 'updated_at']


class PlaceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    latitude = serializers.FloatField(read_only=True)
    longitude = serializers.FloatField(read_only=True)

    class Meta:
        model = Place
        fields = [
            'id', 'name', 'address', 'latitude', 'longitude',
            'category', 'created_at', 'updated_at'
        ]