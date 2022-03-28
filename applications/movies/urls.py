from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('movie/createMovie/', views.MovieCreateApiView.as_view(),
        name="CreateMovie"
    ),
    path('movie/listMovies/', views.MovieListAPIView.as_view(),
        name="ListMovies"
    ),
    path('movie/updateMovie/<pk>/', views.MovieUpdateView.as_view(),
        name="UpdateMovie"
    ),
    path('movie/deleteMovie/<pk>/', views.MovieDeleteView.as_view(),
        name="DeleteMovie"
    ),
]
