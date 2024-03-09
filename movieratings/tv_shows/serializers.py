from rest_framework import serializers

from movies.serializers import UserListSerializer, CelebrityListSerializer
from tv_shows.models import TVShowReviews, TVShowRatings, TVShowCharacters, TVShowVideos, TVShowPhotos, TVShow, \
    PlannedTVShows, TVEpisodeReviews, TVEpisodeRatings, TVEpisodeVideos, TVEpisodePhotos, TVEpisodes, TVShowReviewLikes, \
    TVEpisodeReviewLikes


class TVEpisodeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = ('id', 'slug', 'name', 'poster')


class TVShowReviewsListSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)
    liked = serializers.SerializerMethodField()

    class Meta:
        model = TVShowReviews
        exclude = ('tv_show', )

    def get_liked(self, obj):
        if self.context['request'].user.is_authenticated:
            liked = TVShowReviewLikes.objects.filter(review__id=obj.id, user=self.context['request'].user)
            if liked:
                return True
            return False
        return None


class TVShowRatingsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TVShowRatings
        fields = '__all__'

    def create(self, validated_data):
        rating, created = TVShowRatings.objects.update_or_create(
            user=validated_data.get('user'),
            movie=validated_data.get('tv_show'),
            defaults={'rating': validated_data.get('rating')}
        )

        return rating


class TVShowReviewSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TVShowReviews
        fields = '__all__'


class TVShowCharactersListSerializer(serializers.ModelSerializer):
    celebrity = CelebrityListSerializer(read_only=True)

    class Meta:
        model = TVShowCharacters
        fields = '__all__'


class TVShowCharactersSerializer(serializers.ModelSerializer):

    class Meta:
        model = TVShowCharacters
        fields = '__all__'


class TVShowVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShowVideos
        exclude = ('tv_show', )


class TVShowPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShowPhotos
        exclude = ('tv_show', )


class TVShowPhotosCreateSerializer(serializers.Serializer):
    tv_show = serializers.SlugField()
    photos = serializers.ListField(child=serializers.ImageField())

    def create(self, validated_data):
        photos = validated_data.get('photos')
        tv_show = TVShow.objects.get(slug=validated_data.get('tv_show'))
        photoslist = []
        for photo in photos:
            photoslist.append(TVShowPhotos.objects.create(tv_show=tv_show, photo=photo))
        return {'tv_show': tv_show, 'photos': [instance.photo for instance in photoslist]}


class TVShowVideosCreateSerializer(serializers.Serializer):
    tv_show = serializers.IntegerField()
    videos = serializers.ListField(child=serializers.FileField())

    def create(self, validated_data):
        photos = validated_data.get('videos')
        tv_show = TVShow.objects.get(slug=validated_data.get('tv_show'))
        videoslist = []
        for photo in photos:
            videoslist.append(TVShowVideos.objects.create(tv_show=tv_show, photo=photo))
        return {'tv_show': tv_show, 'videos': [instance.video for instance in videoslist]}


class TVShowSerializer(serializers.ModelSerializer):
    photos = TVShowPhotoSerializer(many=True, read_only=True)
    videos = TVShowVideoSerializer(many=True, read_only=True)
    reviews = TVShowReviewsListSerializer(many=True, read_only=True)
    tvshowcharacters = TVShowCharactersListSerializer(many=True, read_only=True)
    episodes = TVEpisodeListSerializer(many=True, read_only=True)
    country = serializers.SlugRelatedField(slug_field='name', read_only=True)
    languages = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    main_cast = CelebrityListSerializer(many=True, read_only=True)
    actors = CelebrityListSerializer(many=True, read_only=True)
    directors = CelebrityListSerializer(many=True, read_only=True)
    writers = CelebrityListSerializer(many=True, read_only=True)
    user_rating = serializers.SerializerMethodField()

    class Meta:
        model = TVShow
        fields = '__all__'
        read_only_fields = ('slug', 'rating')

    def get_user_rating(self, obj):
        if self.context['request'].user.is_authenticated:
            user_rating = TVShowRatings.objects.filter(tv_show__id=obj.id, user=self.context['request'].user)
            if user_rating:
                return float(user_rating[0].rating)
            return None


class TVShowListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = ('id', 'slug', 'name', 'poster')


class PlannedTVShowSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PlannedTVShows
        fields = ('user', 'tv_show')


class PlannedTVShowListSerializer(serializers.ModelSerializer):
    movie = TVShowListSerializer(read_only=True)

    class Meta:
        model = PlannedTVShows
        fields = ('movie', )


class TVEpisodeReviewsListSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)
    liked = serializers.SerializerMethodField()

    class Meta:
        model = TVEpisodeReviews
        exclude = ('tv_episode', )

    def get_liked(self, obj):
        if self.context['request'].user.is_authenticated:
            liked = TVEpisodeReviewLikes.objects.filter(review__id=obj.id, user=self.context['request'].user)
            if liked:
                return True
            return False
        return None


class TVEpisodeRatingsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TVEpisodeRatings
        fields = '__all__'

    def create(self, validated_data):
        rating, created = TVEpisodeRatings.objects.update_or_create(
            user=validated_data.get('user'),
            movie=validated_data.get('tv_episode'),
            defaults={'rating': validated_data.get('rating')}
        )

        return rating


class TVEpisodeReviewSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TVEpisodeReviews
        fields = '__all__'


class TVEpisodeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVEpisodeVideos
        exclude = ('tv_episode', )


class TVEpisodePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVEpisodePhotos
        exclude = ('tv_episode', )


class TVEpisodePhotosCreateSerializer(serializers.Serializer):
    tv_episode = serializers.SlugField()
    photos = serializers.ListField(child=serializers.ImageField())

    def create(self, validated_data):
        photos = validated_data.get('photos')
        tv_episode = TVEpisodes.objects.get(slug=validated_data.get('tv_episode'))
        photoslist = []
        for photo in photos:
            photoslist.append(TVShowPhotos.objects.create(tv_episode=tv_episode, photo=photo))
        return {'tv_episode': tv_episode, 'photos': [instance.photo for instance in photoslist]}


class TVEpisodeVideosCreateSerializer(serializers.Serializer):
    tv_episode = serializers.IntegerField()
    videos = serializers.ListField(child=serializers.FileField())

    def create(self, validated_data):
        photos = validated_data.get('videos')
        tv_episode = TVEpisodes.objects.get(slug=validated_data.get('tv_show'))
        videoslist = []
        for photo in photos:
            videoslist.append(TVShowVideos.objects.create(tv_episode=tv_episode, photo=photo))
        return {'tv_episode': tv_episode, 'videos': [instance.video for instance in videoslist]}


class TVEpisodesSerializer(serializers.ModelSerializer):
    photos = TVEpisodePhotoSerializer(many=True, read_only=True)
    videos = TVEpisodeVideoSerializer(many=True, read_only=True)
    reviews = TVEpisodeReviewsListSerializer(many=True, read_only=True)
    main_cast = CelebrityListSerializer(many=True, read_only=True)
    actors = CelebrityListSerializer(many=True, read_only=True)
    directors = CelebrityListSerializer(many=True, read_only=True)
    writers = CelebrityListSerializer(many=True, read_only=True)
    user_rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TVEpisodes
        fields = '__all__'
        read_only_fields = ('slug', 'rating')

    def get_user_rating(self, obj):
        if self.context['request'].user.is_authenticated:
            user_rating = TVEpisodeRatings.objects.filter(tv_episode__id=obj.id, user=self.context['request'].user)
            if user_rating:
                return float(user_rating[0].rating)
            return None


class TVShowReviewLikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model =TVShowReviewLikes
        fields = '__all__'


class TVEpisodeReviewLikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model =TVEpisodeReviewLikes
        fields = '__all__'

