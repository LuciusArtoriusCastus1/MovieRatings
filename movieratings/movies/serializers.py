from rest_framework import serializers

from celebrities.models import Celebrity
from custom_user.models import User
from .models import Movies, Languages, Genres, MovieRatings, MovieReviews, MovieCharacters, MovieVideos, MoviePhotos, \
    PlannedMovies, MovieReviewLikes


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'avatar')


class MovieReviewsListSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)
    liked = serializers.SerializerMethodField()

    class Meta:
        model = MovieReviews
        exclude = ('movie', )

    def get_liked(self, obj):
        if self.context['request'].user.is_authenticated:
            liked = MovieReviewLikes.objects.filter(review__id=obj.id, user=self.context['request'].user)
            if liked:
                return True
            return False
        return None


class CelebrityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = ('id', 'slug', 'name', 'image')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'


class MovieRatingsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MovieRatings
        fields = '__all__'

    def create(self, validated_data):
        rating, created = MovieRatings.objects.update_or_create(
            user=validated_data.get('user'),
            movie=validated_data.get('movie'),
            defaults={'rating': validated_data.get('rating')}
        )

        return rating


class MovieReviewSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MovieReviews
        fields = '__all__'


class MovieCharactersListSerializer(serializers.ModelSerializer):
    celebrity = CelebrityListSerializer(read_only=True)

    class Meta:
        model = MovieCharacters
        fields = '__all__'


class MovieCharactersSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieCharacters
        fields = '__all__'


class MovieVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieVideos
        exclude = ('movie', )


class MoviePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviePhotos
        exclude = ('movie', )


class MoviePhotosCreateSerializer(serializers.Serializer):
    movie = serializers.SlugField()
    photos = serializers.ListField(child=serializers.ImageField())

    def create(self, validated_data):
        photos = validated_data.get('photos')
        movie = Movies.objects.get(slug=validated_data.get('movie'))
        photoslist = []
        for photo in photos:
            photoslist.append(MoviePhotos.objects.create(movie=movie, photo=photo))
        return {'movie': movie, 'photos': [instance.photo for instance in photoslist]}


class MovieVideosCreateSerializer(serializers.Serializer):
    movie = serializers.IntegerField()
    videos = serializers.ListField(child=serializers.FileField())

    def create(self, validated_data):
        photos = validated_data.get('videos')
        movie = Movies.objects.get(slug=validated_data.get('movie'))
        videoslist = []
        for photo in photos:
            videoslist.append(MovieVideos.objects.create(movie=movie, photo=photo))
        return {'movie': movie, 'videos': [instance.video for instance in videoslist]}


class MovieSerializer(serializers.ModelSerializer):
    photos = MoviePhotoSerializer(many=True, read_only=True)
    videos = MovieVideoSerializer(many=True, read_only=True)
    reviews = MovieReviewsListSerializer(many=True, read_only=True)
    moviecharacters = MovieCharactersListSerializer(many=True, read_only=True)
    country = serializers.SlugRelatedField(slug_field='name', read_only=True)
    languages = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    main_cast = CelebrityListSerializer(many=True, read_only=True)
    actors = CelebrityListSerializer(many=True, read_only=True)
    directors = CelebrityListSerializer(many=True, read_only=True)
    writers = CelebrityListSerializer(many=True, read_only=True)
    user_rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movies
        fields = '__all__'
        read_only_fields = ('slug', 'rating')

    def get_user_rating(self, obj):
        if self.context['request'].user.is_authenticated:
            user_rating = MovieRatings.objects.filter(movie__id=obj.id, user=self.context['request'].user)
            if user_rating:
                return float(user_rating[0].rating)
            return None


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('id', 'slug', 'name', 'poster')


class PlannedMovieSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PlannedMovies
        fields = ('user', 'movie')


class PlannedMoviesListSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)

    class Meta:
        model = PlannedMovies
        fields = ('movie', )


class MovieReviewLikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MovieReviewLikes
        fields = '__all__'
