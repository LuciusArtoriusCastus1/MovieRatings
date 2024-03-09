from django.urls import path, include
from rest_framework import routers

from movies.documents import MoviesDocumentViewSet, SearchAPI
from movies.views import *

router = routers.DefaultRouter()
router.register(r'genres', GenresViewSet, basename='genres')

router1 = routers.DefaultRouter()
router1.register(r'languages', LanguagesViewSet, basename='languages')

router2 = routers.DefaultRouter()
router2.register(r'moviereviews', MovieReviewsViewSet, basename='moviereviews')

router3 = routers.DefaultRouter()
router3.register(r'movies', MoviesViewSet, basename='movies')

router4 = routers.DefaultRouter()
router4.register(r'moviecharacters', MovieCharactersViewSet, basename='moviecharacters')

router5 = routers.DefaultRouter()
router5.register(r'plannedmovies', PlannedMoviesViewSet, basename='plannedmovies')

router6 = routers.DefaultRouter()
router6.register(r'searchmovies', MoviesDocumentViewSet, basename='searchmovies')

urlpatterns = [
    path('movies/photo/create/', MoviesPhotosCreate.as_view(), name='movies_photo_create'),
    path('movies/photo/delete/<int:pk>/', MoviesPhotosDestroy.as_view(), name='movies_photo_del'),
    path('movies/video/create/', MoviesVideosCreate.as_view(), name='movies_video_create'),
    path('movies/video/delete/<int:pk>/', MoviesVideosDestroy.as_view(), name='movies_video_del'),
    path('movies/ratings/create/', MovieRatingsCreate.as_view(), name='movies_ratings_create'),

    path('movies/review/likes/create/', MovieReviewLikesCreate.as_view(), name='movie_review_likes_create'),
    path('movies/review/likes/delete/<int:pk>/', MovieReviewLikesDestroy.as_view(), name='movie_review_likes_delete'),

    path('search/', SearchAPI.as_view(), name='search'),

    path('', include(router.urls)),
    path('', include(router1.urls)),
    path('', include(router2.urls)),
    path('', include(router3.urls)),
    path('', include(router4.urls)),
    path('', include(router5.urls)),
    path('', include(router6.urls)),
]
