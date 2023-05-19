from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie, Genre
from .serializers import MoviesSerializer

# 로그인 안했을땐 최신영화 보여주기 위한 뷰(홈 큰공간)
@api_view(['GET'])
def latest_movies(request):
    movieList = get_list_or_404(Movie.objects.order_by('-release_date'))
    serializer = MoviesSerializer(movieList[:100], many=True)
    # print(serializer.data)
    return Response(serializer.data)



# 로그인 했을땐 장르별 영화 보여주기 위한 뷰(홈 큰공간)
@api_view(['GET'])
def genre_movies(request):
    movie_list = Movie.objects.order_by('-release_date')[:100]
    serializer = MoviesSerializer(movie_list, many=True)
    response = Response(serializer.data)
    response.accepted_renderer = JSONRenderer()
    return response

# 검색한 영화를 보여줌
@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MoviesSerializer(movie)
    return Response(serializer.data)