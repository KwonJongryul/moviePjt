from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Review
from .serializers import ReviewSerializer, ReviewListSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


# -------------게시글 리스트 불러오기, 게시글 쓰기--------------------------------
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        print(serializer)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            print('??')
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('???')
            print(serializer.errors)

# ----------------게시글 디테일 불러오기, 식제, 수정------------------------------
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = review.user
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.user == user:
        if request.method == 'DELETE':
            print(review)
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        elif request.method == 'PUT':
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    return Response(status=status.HTTP_401_UNAUTHORIZED)