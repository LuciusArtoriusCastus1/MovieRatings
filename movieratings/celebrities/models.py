import datetime

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify

from .services import *


class Celebrity(models.Model):
    name = models.CharField(
        db_index=True,
        max_length=30,
        unique=True,
    )
    slug = models.SlugField(
        db_index=True,
        unique=True,
    )

    image = models.ImageField(
        upload_to=get_celebrity_image,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
        blank=True,
        null=True,
    )
    bio = models.TextField(
        max_length=5000,
        blank=True,
        null=True,
    )

    occupations = models.ManyToManyField(
        'CelebrityOccupations',
        blank=True,
        related_name='celebrities',
    )


    @property
    def age(self):
        bd = str(self.birth_date)
        print(bd[0:4])
        now = int(datetime.datetime.now().year)
        return int(now - int(bd[0:4]))

    birth_date = models.DateField()
    birth_place = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    birth_country = models.ForeignKey(
        'Countries',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='celebrities',
    )
    spouses = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )
    children = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )
    parents = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )

    def save(self):
        self.slug = slugify(self.name)
        super(Celebrity, self).save()

    def __str__(self):
        return self.name


class CelebrityPhotos(models.Model):
    photo = models.ImageField(
        upload_to=get_celebrity_photos,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
    )
    celebrity = models.ForeignKey(
        Celebrity,
        on_delete=models.CASCADE,
        related_name='photos'
    )


class CelebrityVideos(models.Model):
    video = models.FileField(
        upload_to=get_celebrity_videos,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mp3'])],
    )
    celebrity = models.ForeignKey(
        Celebrity,
        on_delete=models.CASCADE,
        related_name='videos'
    )


class CelebrityOccupations(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
    )

    def __str__(self):
        return self.name


class Countries(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
    )

    def __str__(self):
        return self.name
