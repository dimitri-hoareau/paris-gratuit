from rest_framework import viewsets
from .models import Category, Place
from .serializers import CategorySerializer, PlaceSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.select_related('category').all()
    serializer_class = PlaceSerializer