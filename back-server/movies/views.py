from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie, Genre, Comment
from .serializers import MoviesSerializer, GenreSerializer, CommentSerializer
from datetime import datetime
from random import sample
#이것도 추가했어요
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

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

# Review create에서 영화 셀렉트 옵션위한 로직
@api_view(['GET'])
def movies_option(request, keyword):
    movies = Movie.objects.filter(title__contains=keyword)[:10]
    serializer = MoviesSerializer(movies, many=True)
    return Response(serializer.data)

# 시대별 영화를 보여줌
@api_view(['GET'])
def movies_era(request, era):
    if era == '2020':
        start_date = datetime(2020, 1, 1)
        end_date = datetime.now()
    elif era == '2010':
        start_date = datetime(2010, 1, 1)
        end_date = datetime(2019, 12, 31)
    elif era == '2000':
        start_date = datetime(2000, 1, 1)
        end_date = datetime(2009, 12, 31)
    elif era == '1990':
        start_date = datetime(1990, 1, 1)
        end_date = datetime(1999, 12, 31)
    elif era == '1980':
        start_date = datetime(1980, 1, 1)
        end_date = datetime(1989, 12, 31)
    else:
        start_date = datetime(1900, 1, 1)
        end_date = datetime(1979, 12, 31)
    movies = Movie.objects.filter(release_date__range=(start_date, end_date), vote_average__gt=8)
    movies = sample(list(movies), 10)
    serializer = MoviesSerializer(movies, many=True)
    return Response(serializer.data)

# 전체 영화 리스트
@api_view(['GET'])
def movies_all(request):
    movies = get_list_or_404(Movie)
    serializer = MoviesSerializer(movies, many=True)
    return Response(serializer.data)

#전체 장르 리스트
@api_view(['GET'])
def get_genres(request):
    genres = get_list_or_404(Genre)
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

#영화 좋아요 추가
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if movie:
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
        return Response(status=status.HTTP_202_ACCEPTED)

# 코멘트 등록
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment(request):
    print(request.data)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)