from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

from celebrities.permissions import IsAdminOrReadOnly
from .models import Movies, Languages, Genres, MovieRatings, MovieReviews, MovieCharacters, MoviePhotos, MovieVideos, \
    PlannedMovies, MovieReviewLikes
from .serializers import MovieSerializer, LanguageSerializer, GenresSerializer, MovieRatingsSerializer, \
    MovieReviewSerializer, MovieCharactersSerializer, MoviePhotosCreateSerializer, MoviePhotoSerializer, \
    MovieVideosCreateSerializer, MovieVideoSerializer, PlannedMovieSerializer, MovieReviewLikeSerializer


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly]


class LanguagesViewSet(viewsets.ModelViewSet):
    queryset = Languages.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAdminOrReadOnly]


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = [IsAdminOrReadOnly]


class MovieRatingsCreate(CreateAPIView):
    queryset = MovieRatings.objects.all()
    serializer_class = MovieRatingsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MovieReviewsViewSet(viewsets.ModelViewSet):
    queryset = MovieReviews.objects.all()
    serializer_class = MovieReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MovieCharactersViewSet(viewsets.ModelViewSet):
    queryset = MovieCharacters.objects.all()
    serializer_class = MovieCharactersSerializer
    permission_classes = [IsAdminOrReadOnly]


class MoviesPhotosCreate(CreateAPIView):
    queryset = MoviePhotos.objects.all()
    serializer_class = MoviePhotosCreateSerializer
    permission_classes = [IsAdminOrReadOnly]


class MoviesPhotosDestroy(DestroyAPIView):
    queryset = MoviePhotos.objects.all()
    serializer_class = MoviePhotoSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminOrReadOnly]


class MoviesVideosCreate(CreateAPIView):
    queryset = MovieVideos.objects.all()
    serializer_class = MovieVideosCreateSerializer
    permission_classes = [IsAdminOrReadOnly]


class MoviesVideosDestroy(DestroyAPIView):
    queryset = MovieVideos.objects.all()
    serializer_class = MovieVideoSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminOrReadOnly]


class PlannedMoviesViewSet(viewsets.ModelViewSet):
    queryset = PlannedMovies.objects.all()
    serializer_class = PlannedMovieSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly]


class MovieReviewLikesCreate(CreateAPIView):
    queryset = MovieReviewLikes.objects.all()
    serializer_class = MovieReviewLikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MovieReviewLikesDestroy(DestroyAPIView):
    queryset = MovieReviewLikes.objects.all()
    serializer_class = MovieReviewLikeSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly]





