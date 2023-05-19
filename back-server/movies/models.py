from django.db import models
# Create your models here.
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=30)
    genre_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres')
    def __str__(self) -> str:
        return self.name
    
# Create your models here.
class Movie(models.Model):
    adult = models.BooleanField(null=True)
    backdrop_path = models.TextField(null=True)
    genre = models.ManyToManyField(Genre, related_name='genre_movie')
    original_language = models.CharField(max_length=10, null=True)
    original_title = models.TextField(null=True)
    overview = models.TextField(null=True)
    popularity = models.FloatField(null=True)
    poster_path = models.TextField(null=True)
    release_date = models.DateField(null=True)
    title = models.TextField(null=True)
    video = models.BooleanField(null=True)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_moves')
    def __str__(self):
        return self.title

class Actor(models.Model):
    adult = models.BooleanField()
    gender = models.IntegerField()
    department = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    popularity = models.FloatField()
    profile_path = models.TextField(null=True)
    known = models.ManyToManyField(Movie, related_name='actor_movie')
    
    def __str__(self):
        return self.name
