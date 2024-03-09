from rest_framework import serializers
from .models import User
from movies.serializers import PlannedMovieSerializer, PlannedMoviesListSerializer


class UserSerializer(serializers.ModelSerializer):
    rated_movies = serializers.SerializerMethodField(read_only=True)
    planned_movies = PlannedMoviesListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('name', 'email', 'avatar', 'password', 'bio', 'gender', 'rated_movies', 'planned_movies')

    def get_rated_movies(self, obj):

        from movies.serializers import MovieListSerializer

        rated_movies = obj.movieratings.all()
        movielist = []
        for rate in rated_movies:
            movie = MovieListSerializer(rate.movie).data
            movie['user_rating'] = rate.rating
            movielist.append(movie)

        return movielist

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.gender = validated_data.get('gender', instance.gender)
        if validated_data.get('password'):
            instance.set_password(validated_data.get('password'))

        return instance


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'avatar')
