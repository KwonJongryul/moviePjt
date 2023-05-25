from . import views
from django.urls import path

urlpatterns = [
    path('latestmovies/', views.latest_movies),
    path('genremovies/', views.genre_movies),
    path('movies/<int:movie_id>/', views.movie_detail),
    path('movies/option/<str:keyword>/', views.movies_option),
    path('movies/era/<str:era>/', views.movies_era),
    path('movies/genre/<str:genre>/', views.movies_genre),
    path('movies/all/', views.movies_all),
    path('genres/', views.get_genres),
    # path추가했어요-yj
    path('movielike/<int:movie_id>/', views.movie_like),
    path('comment/', views.comment),
    path('comment/<int:pk>/', views.get_comment),
    path('comment/like/<int:pk>/', views.comment_like),
    path('recomment/', views.recomment),
    path('recomment/<int:pk>/', views.recomment_get),
]