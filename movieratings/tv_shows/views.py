from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from celebrities.permissions import IsAdminOrReadOnly
from tv_shows.models import TVShow, TVShowRatings, TVShowReviews, TVShowCharacters, TVShowPhotos, TVShowVideos, \
    PlannedTVShows, TVEpisodes, TVEpisodeRatings, TVEpisodeReviews, TVEpisodePhotos, TVEpisodeVideos, TVShowReviewLikes, \
    TVEpisodeReviewLikes
from tv_shows.serializers import TVShowSerializer, TVShowRatingsSerializer, TVShowReviewSerializer, \
    TVShowCharactersSerializer, TVShowPhotosCreateSerializer, TVShowPhotoSerializer, TVShowVideosCreateSerializer, \
    TVShowVideoSerializer, PlannedTVShowSerializer, TVEpisodesSerializer, TVEpisodeRatingsSerializer, \
    TVEpisodeReviewSerializer, TVEpisodePhotosCreateSerializer, TVEpisodePhotoSerializer, \
    TVEpisodeVideosCreateSerializer, TVEpisodeVideoSerializer, TVShowReviewLikeSerializer, TVEpisodeReviewLikeSerializer


class TVShowViewSet(viewsets.ModelViewSet):
    queryset = TVShow.objects.all()
    serializer_class = TVShowSerializer
    permission_classes = [IsAdminOrReadOnly]


class TVShowRatingsCreate(CreateAPIView):
    queryset = TVShowRatings.objects.all()
    serializer_class = TVShowRatingsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TVShowReviewsViewSet(viewsets.ModelViewSet):
    queryset = TVShowReviews.objects.all()
    serializer_class = TVShowReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TVShowCharactersViewSet(viewsets.ModelViewSet):
    queryset = TVShowCharacters.objects.all()
    serializer_class = TVShowCharactersSerializer
    permission_classes = [IsAdminOrReadOnly]


class TVShowPhotosCreate(CreateAPIView):
    queryset = TVShowPhotos.objects.all()
    serializer_class = TVShowPhotosCreateSerializer
    permission_classes = [IsAdminOrReadOnly]


class TVShowPhotosDestroy(DestroyAPIView):
    queryset = TVShowPhotos.objects.all()
    serializer_class = TVShowPhotoSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminOrReadOnly]


class TVShowVideosCreate(CreateAPIView):
    queryset = TVShowVideos.objects.all()
    serializer_class = TVShowVideosCreateSerializer
    permission_classes = [IsAdminOrReadOnly]


class TVShowVideosDestroy(DestroyAPIView):
    queryset = TVShowVideos.objects.all()
    serializer_class = TVShowVideoSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminOrReadOnly]


class PlannedTVShowViewSet(viewsets.ModelViewSet):
    queryset = PlannedTVShows.objects.all()
    serializer_class = PlannedTVShowSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly]


class TVEpisodesViewSet(viewsets.ModelViewSet):
    queryset = TVEpisodes.objects.all()
    serializer_class = TVEpisodesSerializer
    permission_classes = [IsAdminOrReadOnly]


class TVEpisodeRatingsCreate(CreateAPIView):
    queryset = TVEpisodeRatings.objects.all()
    serializer_class = TVEpisodeRatingsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TVEpisodeReviewsViewSet(viewsets.ModelViewSet):
    queryset = TVEpisodeReviews.objects.all()
    serializer_class = TVEpisodeReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TVEpisodePhotosCreate(CreateAPIView):
    queryset = TVEpisodePhotos.objects.all()
    serializer_class = TVEpisodePhotosCreateSerializer
    permission_classes = [IsAdminOrReadOnly]


class TVEpisodePhotosDestroy(DestroyAPIView):
    queryset = TVEpisodePhotos.objects.all()
    serializer_class = TVEpisodePhotoSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminOrReadOnly]


class TVEpisodeVideosCreate(CreateAPIView):
    queryset = TVEpisodeVideos.objects.all()
    serializer_class = TVEpisodeVideosCreateSerializer
    permission_classes = [IsAdminOrReadOnly]


class TVEpisodeVideosDestroy(DestroyAPIView):
    queryset = TVEpisodeVideos.objects.all()
    serializer_class = TVEpisodeVideoSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminOrReadOnly]


class TVShowReviewLikesCreate(CreateAPIView):
    queryset = TVShowReviewLikes.objects.all()
    serializer_class = TVShowReviewLikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TVShowReviewLikesDestroy(DestroyAPIView):
    queryset = TVShowReviewLikes.objects.all()
    serializer_class = TVShowReviewLikeSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly]


class TVEpisodeReviewLikesCreate(CreateAPIView):
    queryset = TVEpisodeReviewLikes.objects.all()
    serializer_class = TVEpisodeReviewLikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TVEpisodeReviewLikesDestroy(DestroyAPIView):
    queryset = TVEpisodeReviewLikes.objects.all()
    serializer_class = TVEpisodeReviewLikeSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly]

