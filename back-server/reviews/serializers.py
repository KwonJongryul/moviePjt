from rest_framework import serializers
from .models import Review
from django.contrib.auth import get_user_model
class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta :
        model = Review
        fields = '__all__'
        
        
class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    watch_date = serializers.CharField(read_only=False)
    class Meta :
        model = Review
        fields = '__all__'
        read_only_fields = ('user', )
        
class UserSerializer(serializers.ModelSerializer):
    user_img = serializers.ImageField(required=False)
    class Meta :
        model = get_user_model()
        fields = '__all__'