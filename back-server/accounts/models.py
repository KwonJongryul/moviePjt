from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Genre

# Create your models here.

class User(AbstractUser):
    user_img = models.ImageField(upload_to='user_images/', default='user_images/default.jpg')
    like_genres = models.ManyToManyField(Genre, related_name='genre_users')
    One_liner = models.CharField(max_length=100, default='안녕하세요!')