from django.db import models
from django.conf import settings
from movies.models import Movie
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_reviews')
    title = models.CharField(max_length=50)
    vote = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    context = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    watch_date = models.DateField(auto_now=True)
    watch_with = models.CharField(max_length=50)
    quotes = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews', blank=True)
    def __str__(self):
        return self.title