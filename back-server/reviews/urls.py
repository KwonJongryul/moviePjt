from . import views
from django.urls import path

urlpatterns = [
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('like/<int:review_pk>/', views.review_like),
    path('getid/', views.get_id),
    path('getuser/<int:pk>/', views.get_user),
    path('upload/', views.upload_img),    
    path('<int:user_pk>/follow/', views.follow),
]