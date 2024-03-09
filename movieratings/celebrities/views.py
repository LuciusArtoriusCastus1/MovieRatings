from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework import viewsets
from .models import Celebrity, CelebrityVideos, CelebrityPhotos, CelebrityOccupations, Countries
from .permissions import IsAdminOrReadOnly
from .serializers import CelebritiesSerializer, CelebrityPhotosCreateSerializer, CelebrityVideosCreateSerializer, \
    CelebrityPhotoSerializer, CelebrityVideoSerializer, CelebrityOccupationSerializer, CountrySerializer


class CelebritiesViewSet(viewsets.ModelViewSet):
    queryset = Celebrity.objects.all()
    serializer_class = CelebritiesSerializer
    permission_classes = [IsAdminOrReadOnly]


class CelebrityPhotosCreate(CreateAPIView):
    queryset = CelebrityPhotos.objects.all()
    serializer_class = CelebrityPhotosCreateSerializer
    permission_classes = [IsAdminOrReadOnly]


class CelebrityPhotosDestroy(DestroyAPIView):
    queryset = CelebrityPhotos.objects.all()
    serializer_class = CelebrityPhotoSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminOrReadOnly]


class CelebrityVideosCreate(CreateAPIView):
    queryset = CelebrityVideos.objects.all()
    serializer_class = CelebrityVideosCreateSerializer
    permission_classes = [IsAdminOrReadOnly]


class CelebrityVideosDestroy(DestroyAPIView):
    queryset = CelebrityVideos.objects.all()
    serializer_class = CelebrityVideoSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminOrReadOnly]


class CelebrityOccupationsViewSet(viewsets.ModelViewSet):
    queryset = CelebrityOccupations.objects.all()
    serializer_class = CelebrityOccupationSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminOrReadOnly]


class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminOrReadOnly]