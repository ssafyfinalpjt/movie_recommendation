import json
from .models import Movie, Genre, Actor, MovieReview
from django.http import HttpResponse, JsonResponse
from .serializers import MovieSerializer, ReviewSerializer
# from .serializers import MovieDetailSerializer, GenreSerializer
from rest_framework import status
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET'])
def movie_list(request):
    with open('movies/fixtures/movies.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return JsonResponse(data, safe=False)
    # movies = Movie.objects.all()
    # serializer = MovieSerializer(movies)
    # print(serializer.data)
    # return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_id):

    # movie = Movie.objects.get(movie_id=movie_id)

    # serializer = MovieSerializer(movie)
    # print(serializer.data)
    # return Response(serializer.data)



    with open('movies/fixtures/movies.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    movie = None
    for item in data:
        if item['pk'] == movie_id:
            movie = item
            break
    if not movie:
        return Response(status=status.HTTP_404_NOT_FOUND)
    is_liked = False
    if request.user:
        if movie['fields']['actors'] and request.user.pk in movie['fields']['actors']:
            is_liked = True
        else:
            is_liked = False
    context = {
        'data': movie,
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
@permission_classes([IsAuthenticated])
def movie_likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    serializer = MovieSerializer(movie)  
    return Response(serializer.data)



@api_view(['GET'])
def search_movies(request):
    q = request.GET.get('q', '')
    qs = Movie.objects.none()
    if q:
        qs = Movie.objects.filter(Q(title__icontains=q))
    serializer = MovieSerializer(qs, many=True)
    return Response(serializer.data)



def genre(request):
    with open('movies/fixtures/genre.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return JsonResponse(data, safe=False)


def signupgenre(request):
    with open('movies/fixtures/genre.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return JsonResponse(data, safe=False)
