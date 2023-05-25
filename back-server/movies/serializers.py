from rest_framework import serializers
from .models import Movie, Genre, Comment, Recomment
        
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ReCommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Recomment
        fields = '__all__'
        read_only_fields = ('user', )

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    recomments = serializers.SerializerMethodField()
    
    def get_recomments(self, instance):
        recomments = instance.recomments.all()  # 역참조된 comment 객체들을 가져옴
        serializer = ReCommentSerializer(recomments, many=True)  # CommentSerializer로 직렬화
        return serializer.data
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', )

class MoviesSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    def get_comments(self, instance):
        comments = instance.comments.all()  # 역참조된 comment 객체들을 가져옴
        serializer = CommentSerializer(comments, many=True)  # CommentSerializer로 직렬화
        return serializer.data
    
    class Meta :
        model = Movie
        fields = '__all__'