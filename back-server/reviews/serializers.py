from rest_framework import serializers
from .models import Review

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