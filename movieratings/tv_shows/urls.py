from django.urls import include, path
from rest_framework import routers

from tv_shows.documents import TVShowDocumentViewSet
from tv_shows.views import TVShowViewSet, TVShowPhotosCreate, TVEpisodesViewSet, TVShowPhotosDestroy, \
    TVShowVideosCreate, TVShowVideosDestroy, TVShowRatingsCreate, TVEpisodePhotosCreate, TVEpisodeVideosCreate, \
    TVEpisodePhotosDestroy, TVEpisodeVideosDestroy, TVEpisodeRatingsCreate, TVShowCharactersViewSet, \
    TVShowReviewsViewSet, PlannedTVShowViewSet, TVEpisodeReviewsViewSet, TVShowReviewLikesCreate, \
    TVShowReviewLikesDestroy, TVEpisodeReviewLikesDestroy, TVEpisodeReviewLikesCreate

router = routers.DefaultRouter()
router.register(r'tvshows', TVShowViewSet, basename='tvshows')

router1 = routers.DefaultRouter()
router1.register(r'tvepisodes', TVEpisodesViewSet, basename='tvepisodes')

router2 = routers.DefaultRouter()
router2.register(r'tvshowcharacters', TVShowCharactersViewSet, basename='tvshowcharacters')

router3 = routers.DefaultRouter()
router3.register(r'tvshowreviews', TVShowReviewsViewSet, basename='tvshowreviews')

router4 = routers.DefaultRouter()
router4.register(r'plannedtvshows', PlannedTVShowViewSet, basename='plannedtvshows')

router5 = routers.DefaultRouter()
router5.register(r'tvepisodereviews', TVEpisodeReviewsViewSet, basename='tvepisodereviews')

router6 = routers.DefaultRouter()
router6.register(r'searchtvshow', TVShowDocumentViewSet, basename='searchtvshow')


urlpatterns = [
    path('tvshows/photo/create/', TVShowPhotosCreate.as_view(), name='tvshow_photo_create'),
    path('tvshows/photo/delete/<int:pk>/', TVShowPhotosDestroy.as_view(), name='tvshow_photo_delete'),
    path('tvshows/video/create/', TVShowVideosCreate.as_view(), name='tvshow_video_create'),
    path('tvshows/photo/delete/<int:pk>/', TVShowVideosDestroy.as_view(), name='tvshow_photo_delete'),
    path('tvshows/ratings/create/', TVShowRatingsCreate.as_view(), name='tvshow_rating_create'),

    path('tvepisodes/photo/create/', TVEpisodePhotosCreate.as_view(), name='tvepisode_photo_create'),
    path('tvepisodes/photo/delete/<int:pk>/', TVEpisodePhotosDestroy.as_view(), name='tvepisode_photo_delete'),
    path('tvepisodes/video/create/', TVEpisodeVideosCreate.as_view(), name='tvepisode_video_create'),
    path('tvepisodes/photo/delete/<int:pk>/', TVEpisodeVideosDestroy.as_view(), name='tvepisode_video_delete'),
    path('tvepisodes/ratings/cerate/', TVEpisodeRatingsCreate.as_view(), name='tvepisode_rating_create'),

    path('tvshows/review/likes/create/', TVShowReviewLikesCreate.as_view(), name='tvshow_review_likes_create'),
    path('tvshows/review/likes/delete/<int:pk>/', TVShowReviewLikesDestroy.as_view(), name='tvshow_review_likes_delete'),
    path('tvepisodes/review/likes/create/', TVEpisodeReviewLikesCreate.as_view(), name='tvepisode_review_likes_create'),
    path('tvepisodes/review/likes/delete/<int:pk>/', TVEpisodeReviewLikesDestroy.as_view(), name='tvepisode_review_likes_delete'),

    path('', include(router.urls)),
    path('', include(router1.urls)),
    path('', include(router2.urls)),
    path('', include(router3.urls)),
    path('', include(router4.urls)),
    path('', include(router5.urls)),
    path('', include(router6.urls)),
]