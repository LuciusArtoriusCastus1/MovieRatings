from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg, F
from django.utils.text import slugify

from celebrities.models import Celebrity, Countries
from custom_user.models import User
from movies.models import Genres, Languages
from tv_shows.services import get_tv_show_poster, get_tv_show_photo, get_tv_show_video, get_tv_show_trailer, \
    get_tv_episode_video, get_tv_episode_photo, get_tv_episode_poster, get_tv_episode_trailer


class TVShow(models.Model):
    name = models.CharField(max_length=30, unique=True, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)
    poster = models.ImageField(upload_to=get_tv_show_poster, validators=[FileExtensionValidator(['jpg', 'png'])])
    description = models.TextField(max_length=8000, blank=True, null=True)
    season = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1)])
    episodes_count = models.PositiveIntegerField(blank=True, null=True)
    release_start_date = models.DateField(blank=True, null=True)
    release_end_date = models.DateField(blank=True, null=True)
    released = models.BooleanField()
    ongoing = models.BooleanField()
    genres = models.ManyToManyField(Genres, blank=True, related_name='tv_shows')
    country = models.ForeignKey(Countries, on_delete=models.SET_NULL, null=True, blank=True)
    languages = models.ManyToManyField(Languages, blank=True, related_name='tv_shows')
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True,
                                 validators=[MinValueValidator(1), MaxValueValidator(10)])
    trailer = models.FileField(upload_to=get_tv_show_trailer, validators=[FileExtensionValidator(['mp4', 'mp3'])])
    main_cast = models.ManyToManyField(Celebrity, blank=True, related_name='mainactorshows')
    actors = models.ManyToManyField(Celebrity, blank=True, related_name='actorshows')
    directors = models.ManyToManyField(Celebrity, blank=True, related_name='directorshows')
    producers = models.ManyToManyField(Celebrity, blank=True, related_name='producershows')
    writers = models.ManyToManyField(Celebrity, blank=True, related_name='writershows')
    budget = models.PositiveIntegerField(blank=True, null=True)
    box_office = models.PositiveIntegerField(blank=True, null=True)
    posted = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(TVShow, self).save()


class TVShowPhotos(models.Model):
    tv_show = models.ForeignKey(
        TVShow,
        on_delete=models.CASCADE,
        related_name='photos',
    )
    photo = models.ImageField(
        upload_to=get_tv_show_photo,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
    )


class TVShowVideos(models.Model):
    tv_show = models.ForeignKey(
        TVShow,
        on_delete=models.CASCADE,
        related_name='videos',
    )
    video = models.FileField(
        upload_to=get_tv_show_video,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mp3'])],
    )


class TVShowReviews(models.Model):
    review = models.CharField(
        max_length=1000,
    )
    tv_show = models.ForeignKey(
        TVShow,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tvshowreviews'
    )
    likes = models.PositiveIntegerField(default=0)
    posted = models.DateTimeField(
        auto_now_add=True,
    )
    edited = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.review


class TVShowRatings(models.Model):
    tv_show = models.ForeignKey(
        TVShow,
        on_delete=models.CASCADE,
        related_name='ratings',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tvshowratings'
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    posted = models.DateTimeField(
        auto_now_add=True,
    )
    edited = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return str(self.rating)

    def save(self, *args, **kwargs):
        super(TVShowRatings, self).save(*args, **kwargs)

        tv_show = TVShow.objects.get(id=self.tv_show.id)
        rating = tv_show.ratings.aggregate(rating=Avg('rating'))['rating']
        tv_show.rating = rating
        tv_show.save()

    def delete(self, *args, **kwargs):
        super(TVShowRatings, self).delete(*args, **kwargs)

        tv_show = TVShow.objects.get(id=self.tv_show.id)
        rating = tv_show.ratings.aggregate(rating=Avg('rating'))['rating']
        tv_show.rating = rating
        tv_show.save()


class TVShowCharacters(models.Model):
    name = models.CharField(
        max_length=50,
    )
    tv_show = models.ForeignKey(
        TVShow,
        on_delete=models.CASCADE,
        related_name='tvshowcharacters'
    )
    celebrity = models.ForeignKey(
        Celebrity,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='tvshowcharacters'
    )

    def __str__(self):
        return self.name


class PlannedTVShows(models.Model):
    tv_show = models.ForeignKey(TVShow, on_delete=models.CASCADE, related_name='planned_tvshows')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='planned_tvshows')


class TVEpisodes(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField()
    tv_show = models.ForeignKey(TVShow, on_delete=models.CASCADE, related_name='episodes')
    description = models.TextField(max_length=8000)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True,
                                 validators=[MinValueValidator(1), MaxValueValidator(10)])
    trailer = models.FileField(upload_to=get_tv_show_trailer, validators=[FileExtensionValidator(['mp4', 'mp3'])])
    poster = models.ImageField(upload_to=get_tv_episode_poster,
                               validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])])
    trailer = models.FileField(upload_to=get_tv_episode_trailer,
                               validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mp3'])])
    released = models.BooleanField(default=True)
    release_date = models.DateField()
    runtime = models.PositiveIntegerField(blank=True, null=True)

    posted = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(TVEpisodes, self).save()


class TVEpisodePhotos(models.Model):
    tv_episode = models.ForeignKey(
        TVEpisodes,
        on_delete=models.CASCADE,
        related_name='photos',
    )
    photo = models.ImageField(
        upload_to=get_tv_episode_photo,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
    )


class TVEpisodeVideos(models.Model):
    tv_episode = models.ForeignKey(
        TVEpisodes,
        on_delete=models.CASCADE,
        related_name='videos',
    )
    video = models.FileField(
        upload_to=get_tv_episode_video,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mp3'])],
    )


class TVEpisodeReviews(models.Model):
    review = models.CharField(
        max_length=1000,
    )
    tv_episode = models.ForeignKey(
        TVEpisodes,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tvepisodereviews'
    )
    likes = models.PositiveIntegerField(default=0)
    posted = models.DateTimeField(
        auto_now_add=True,
    )
    edited = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.review


class TVEpisodeRatings(models.Model):
    tv_episode = models.ForeignKey(
        TVEpisodes,
        on_delete=models.CASCADE,
        related_name='ratings',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tvepisoderatings'
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    posted = models.DateTimeField(
        auto_now_add=True,
    )
    edited = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return str(self.rating)

    def save(self, *args, **kwargs):
        super(TVEpisodeRatings, self).save(*args, **kwargs)

        tv_episode = TVEpisodes.objects.get(id=self.tv_episode.id)
        rating = tv_episode.ratings.aggregate(rating=Avg('rating'))['rating']
        tv_episode.rating = rating
        tv_episode.save()

    def delete(self, *args, **kwargs):
        super(TVEpisodeRatings, self).delete(*args, **kwargs)

        tv_episode = TVEpisodes.objects.get(id=self.tv_episode.id)
        rating = tv_episode.ratings.aggregate(rating=Avg('rating'))['rating']
        tv_episode.rating = rating
        tv_episode.save()


class TVShowReviewLikes(models.Model):
    review = models.ForeignKey(TVShowReviews, on_delete=models.CASCADE, related_name='review_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tv_show_review_likes')
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.review} - {self.user} - {self.posted}'

    def save(self, *args, **kwargs):
        super(TVShowReviewLikes, self).save(*args, **kwargs)

        TVShowReviews.objects.filter(user=self.user, id=self.review.id).update(likes=F('likes') + 1)

    def delete(self, *args, **kwargs):
        super(TVShowReviewLikes, self).delete(*args, **kwargs)

        TVShowReviews.objects.filter(user=self.user, id=self.review.id).update(likes=F('likes') - 1)


class TVEpisodeReviewLikes(models.Model):
    review = models.ForeignKey(TVEpisodeReviews, on_delete=models.CASCADE, related_name='review_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tv_episode_review_likes')
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.review} - {self.user} - {self.posted}'

    def save(self, *args, **kwargs):
        super(TVEpisodeReviewLikes, self).save(*args, **kwargs)

        TVShowReviews.objects.filter(user=self.user, id=self.review.id).update(likes=F('likes') + 1)

    def delete(self, *args, **kwargs):
        super(TVEpisodeReviewLikes, self).delete(*args, **kwargs)

        TVShowReviews.objects.filter(user=self.user, id=self.review.id).update(likes=F('likes') - 1)