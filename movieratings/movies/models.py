from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Sum, Avg, F
from django.utils.text import slugify
from celebrities.models import Celebrity, Countries
from custom_user.models import User
from .services import get_movie_photo, get_movie_video, get_movie_trailer, get_movie_poster


class Movies(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        db_index=True,
    )
    slug = models.SlugField(
        unique=True,
        db_index=True,
    )
    poster = models.ImageField(
        upload_to=get_movie_poster,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])],
    )
    description = models.TextField(
        blank=True,
        null=True,
        max_length=10000
    )
    released = models.BooleanField()
    release_date = models.DateField(
        blank=True,
        null=True,
    )

    genres = models.ManyToManyField(
        'Genres',
        blank=True,
        related_name='movies',
    )
    country = models.ForeignKey(
        Countries,
        blank=True,
        null=True,
        related_name='movies',
        on_delete=models.SET_NULL
    )
    languages = models.ManyToManyField(
        'Languages',
        blank=True,
        related_name='movies',
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    trailer = models.FileField(
        upload_to=get_movie_trailer,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mp3'])],
    )
    main_cast = models.ManyToManyField(
        Celebrity,
        blank=True,
        related_name='mainactormovies',
    )
    actors = models.ManyToManyField(
        Celebrity,
        blank=True,
        related_name='actormovies',
    )
    directors = models.ManyToManyField(
        Celebrity,
        blank=True,
        related_name='directormovies',
    )
    writers = models.ManyToManyField(
        Celebrity,
        blank=True,
        related_name='writermovies',
    )
    producers = models.ManyToManyField(
        Celebrity,
        blank=True,
        related_name='producermovies',
    )
    budget = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    box_office = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    runtime = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    posted = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movies, self).save()


class Genres(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
    )

    def __str__(self):
        return self.name


class Languages(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True
    )

    def __str__(self):
        return self.name


class MoviePhotos(models.Model):
    movie = models.ForeignKey(
        Movies,
        on_delete=models.CASCADE,
        related_name='photos',
    )
    photo = models.ImageField(
        upload_to=get_movie_photo,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
    )


class MovieVideos(models.Model):
    movie = models.ForeignKey(
        Movies,
        on_delete=models.CASCADE,
        related_name='videos',
    )
    video = models.FileField(
        upload_to=get_movie_video,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mp3'])],
    )


class MovieReviews(models.Model):
    review = models.CharField(
        max_length=1000,
    )
    movie = models.ForeignKey(
        Movies,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='moviereviews'
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


class MovieRatings(models.Model):
    movie = models.ForeignKey(
        Movies,
        on_delete=models.CASCADE,
        related_name='ratings',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='movieratings'
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
        super(MovieRatings, self).save(*args, **kwargs)

        movie = Movies.objects.get(id=self.movie.id)
        rating = movie.ratings.aggregate(rating=Avg('rating'))['rating']
        movie.rating = rating
        movie.save()

    def delete(self, *args, **kwargs):
        super(MovieRatings, self).delete(*args, **kwargs)

        movie = Movies.objects.get(id=self.movie.id)
        rating = movie.ratings.aggregate(rating=Avg('rating'))['rating']
        movie.rating = rating
        movie.save()


class MovieCharacters(models.Model):
    name = models.CharField(
        max_length=50,
    )
    movie = models.ForeignKey(
        Movies,
        on_delete=models.CASCADE,
        related_name='moviecharacters'
    )
    celebrity = models.ForeignKey(
        Celebrity,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='moviecharacters'
    )

    def __str__(self):
        return self.name


class PlannedMovies(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='planned_movies')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='planned_movies')


class MovieReviewLikes(models.Model):
    review = models.ForeignKey(MovieReviews, on_delete=models.CASCADE, related_name='review_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movie_review_likes')
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.review} - {self.user} - {self.posted}'

    def save(self, *args, **kwargs):
        super(MovieReviewLikes, self).save(*args, **kwargs)

        MovieReviews.objects.filter(user=self.user, id=self.review.id).update(likes=F('likes') + 1)

    def delete(self, *args, **kwargs):
        super(MovieReviewLikes, self).delete(*args, **kwargs)

        MovieReviews.objects.filter(user=self.user, id=self.review.id).update(likes=F('likes') - 1)



