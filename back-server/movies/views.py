from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie, Genre
from .serializers import MoviesSerializer

@api_view(['GET'])
def movies(request):
    movieList = get_list_or_404(Movie)
    serializer = MoviesSerializer(movieList, many=True)
    return Response(serializer.data)