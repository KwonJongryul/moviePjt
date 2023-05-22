from . import views
from django.urls import path

urlpatterns = [
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('like/<int:review_pk>/', views.review_like),
]