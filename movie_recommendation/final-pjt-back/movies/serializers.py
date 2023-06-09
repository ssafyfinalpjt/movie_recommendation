from rest_framework import serializers
from .models import Movie, Genre, Actor, MovieReview
from django.contrib.auth import get_user_model
User = get_user_model()

class GenrenameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name',)

class ActornameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name','profile_path')

class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_users', 'actors')

    def get_genres(self, obj):
        return [genre.name for genre in obj.genres.all()]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields = ('id', 'title','content')

class UserSerializer(serializers.ModelSerializer):
    like_movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'like_movies',)