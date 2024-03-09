from rest_framework.fields import SerializerMethodField
from rest_framework import serializers

from celebrities.models import *
from movies.serializers import (MovieListSerializer, )
from tv_shows.serializers import TVShowListSerializer


class CelebrityVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CelebrityVideos
        exclude = ('celebrity', )


class CelebrityPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CelebrityPhotos
        exclude = ('celebrity', )


class CelebritiesSerializer(serializers.ModelSerializer):
    age = SerializerMethodField()
    photos = CelebrityPhotoSerializer(many=True, read_only=True)
    videos = CelebrityVideoSerializer(many=True, read_only=True)
    actormovies = MovieListSerializer(many=True, read_only=True)
    directormovies = MovieListSerializer(many=True, read_only=True)
    producermovies = MovieListSerializer(many=True, read_only=True)
    mainactormovies = MovieListSerializer(many=True, read_only=True)
    actorshows = TVShowListSerializer(many=True, read_only=True)
    directorshows = TVShowListSerializer(many=True, read_only=True)
    producershows = TVShowListSerializer(many=True, read_only=True)
    mainactorshows = TVShowListSerializer(many=True, read_only=True)

    class Meta:
        model = Celebrity
        fields = '__all__'

    def get_age(self, obj):
        return obj.age


class CelebrityPhotosCreateSerializer(serializers.Serializer):
    celebrity = serializers.SlugField()
    photos = serializers.ListField(child=serializers.ImageField())

    def create(self, validated_data):
        photos = validated_data.get('photos')
        celebrity = Celebrity.objects.get(slug=validated_data.get('celebrity'))
        photoslist = []
        for photo in photos:
            photoslist.append(CelebrityPhotos.objects.create(celebrity=celebrity, photo=photo))
        return {'celebrity': celebrity, 'photos': [instance.photo for instance in photoslist]}


class CelebrityVideosCreateSerializer(serializers.Serializer):
    celebrity = serializers.IntegerField()
    videos = serializers.ListField(child=serializers.FileField())

    def create(self, validated_data):
        photos = validated_data.get('videos')
        celebrity = Celebrity.objects.get(slug=validated_data.get('celebrity'))
        videoslist = []
        for photo in photos:
            videoslist.append(CelebrityVideos.objects.create(celebrity=celebrity, photo=photo))
        return {'celebrity': celebrity, 'videos': [instance.video for instance in videoslist]}


class CelebrityOccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CelebrityOccupations
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = '__all__'

