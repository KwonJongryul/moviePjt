from django.db import models
# Create your models here.
from django.contrib.postgres.fields import ArrayField

class Genre(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.name
    
# Create your models here.
class Movie(models.Model):
    adult = models.BooleanField()
    backdrop_path = models.TextField(null=True)
    genre = models.ManyToManyField(Genre, related_name='genre_movie')
    id = models.IntegerField(primary_key=True)
    original_language = models.CharField(max_length=10)
    original_title = models.TextField()
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.TextField(null=True)
    release_date = models.DateField()
    title = models.TextField()
    video = models.BooleanField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    
    def __str__(self):
        return self.title

# class Cast(models.Model):