from . import views
from django.urls import path

urlpatterns = [
    path('reviews/', views.review_list),
]