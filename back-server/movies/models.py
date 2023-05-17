from django.db import models
# Create your models here.


class Genre(models.Model):
    genre_id = models.IntegerField()
    name = models.CharField(max_length=30)

# Create your models here.
class Movie(models.Model):
    adult = models.BooleanField()
    backdrop_path = models.TextField(null=True)
    genre_ids = models.TextField()
    id = models.IntegerField(primary_key=True)
    original_language = models.CharField(max_length=10)
    original_title = models.TextField()
    overview = models.TextField()
    popularity = models.TextField()
    poster_path = models.TextField(null=True)
    release_date = models.DateField()
    title = models.TextField()
    video = models.BooleanField()
    vote_average = models.TextField()
    vote_count = models.IntegerField()
    
    def __str__(self):
        return self.title

# class Cast(models.Model):