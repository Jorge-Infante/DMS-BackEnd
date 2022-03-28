from django.shortcuts import render

# Create your views here.

# Importación librerias django rest framework
from rest_framework.generics import (
    CreateAPIView,ListAPIView, RetrieveUpdateAPIView, DestroyAPIView
)
# Importación modelo tarea
from . models import Movie

# Importación serializador para tareas
from . serializers import MovieSerializer

class MovieCreateApiView(CreateAPIView):
    """Create a movie""" 

    serializer_class = MovieSerializer

class MovieListAPIView(ListAPIView):
    """List movies"""

    serializer_class = MovieSerializer
    def get_queryset(self):
        return Movie.objects.all()

class MovieUpdateView(RetrieveUpdateAPIView):
    """Update a movie"""
    
    serializer_class = MovieSerializer
    queryset= Movie.objects.all()

class MovieDeleteView(DestroyAPIView):
    """Delete a movie"""
    serializer_class = MovieSerializer
    queryset= Movie.objects.all()