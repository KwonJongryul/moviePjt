from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Review
from .serializers import ReviewSerializer, ReviewListSerializer, UserSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework.parsers import MultiPartParser


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
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)

# ----------------게시글 디테일 불러오기, 식제, 수정------------------------------
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        print(request.data)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return Response(status=status.HTTP_202_ACCEPTED)

# 현재 유저 정보 불러오기
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_id(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


# 선택 유저 정보 불러오기
@api_view(['POST', 'PUT'])
@permission_classes([IsAuthenticated])
def get_user(request, pk):
    USER = get_user_model()
    user = get_object_or_404(USER, pk=pk)
    if request.method == 'POST':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        user_img = request.FILES.get('user_img')
        if user_img:
            request.data['user_img'] = user_img
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors,'--------------------', serializer.data)
        # print(request.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

# 프로필 사진 업로드
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_img(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        file_path = default_storage.save('user_imges/' + file.name, ContentFile(file.read()))
        return file_path  # 파일의 경로 반환
    else:
        return None