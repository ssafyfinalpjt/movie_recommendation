import json
from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieSerializer, ReviewSerializer
# from .serializers import ReviewSerializer, MovieDetailSerializer, GenreSerializer
from .models import Movie, Genre, Actor, MovieReview
# Create your views here.

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_id):
<<<<<<< HEAD
    movie = get_object_or_404(Movie.objects.prefetch_related('actors','genres'), pk=movie_id)
=======
    movie = get_object_or_404(Movie.objects.prefetch_related('actors','genres','directors', 'ott_paths'), movie_id=movie_id)
>>>>>>> e5adabd9b36d9ec7f0a03b4c4e7510b9370002ac

    serializer = MovieSerializer(movie)

    is_liked = False

    if request.user:
        if movie.like_users.filter(pk=request.user.pk).exists():
            is_liked = True
        else:
            is_liked = False

    context = {
        'data': serializer.data,
        'is_liked': is_liked
    }

    return Response(context)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_create(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def review_list(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    review = movie.reviews.all()
    serializer = ReviewSerializer(review, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def movie_likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return


def your_view_function(request):
    with open('movies/fixtures/movies.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return JsonResponse(data, safe=False)
