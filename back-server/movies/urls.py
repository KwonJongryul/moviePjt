from . import views
from django.urls import path

urlpatterns = [
    path('latestmovies/', views.latest_movies),
    path('genremovies/', views.genre_movies),
    path('movies/<int:movie_id>/', views.movie_detail),
    path('movies/option/<str:keyword>/', views.movies_option),
    path('movies/era/<str:era>', views.movies_era),
    path('movies/all/', views.movies_all),
    path('genres/', views.get_genres),
    # path추가했어요-yj
    path('movielike/<int:movie_id>/', views.movie_like),
    path('comment/', views.comment),
]