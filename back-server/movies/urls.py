from . import views
from django.urls import path

urlpatterns = [
    path('movies/', views.movies),
]