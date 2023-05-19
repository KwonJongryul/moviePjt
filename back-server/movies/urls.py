from . import views
from django.urls import path

urlpatterns = [
    path('latestmovies/', views.latest_movies),
    path('genremovies/', views.genre_movies),
    path('movies/<int:movie_id>', views.movie_detail)
]