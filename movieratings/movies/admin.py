from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'release_date', 'rating', 'country', 'budget', 'box_office', 'runtime')
    search_fields = ('name', 'slug', 'description')
    list_filter = ('name', 'release_date', 'rating', 'country', 'budget', 'box_office', 'runtime')
    ordering = ('name', 'release_date', 'posted', 'edited', 'rating', 'budget', 'box_office', 'runtime')
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    readonly_fields = ('rating', )


@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )
    ordering = ('name', )
    save_on_top = True


@admin.register(MoviePhotos)
class MoviePhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'get_photo')
    list_filter = ('movie', )
    ordering = ('movie', )
    save_on_top = True
    search_fields = ('movie', )

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=70 style='border-radius: 10px;'>")


@admin.register(MovieVideos)
class MovieVideosAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'get_video')
    list_filter = ('movie',)
    ordering = ('movie',)
    save_on_top = True
    search_fields = ('movie',)

    def get_video(self, obj):
        if obj.video:
            return mark_safe(f"<video src='{obj.video.url}' width=70 style='border-radius: 10px;'>")


@admin.register(MovieReviews)
class MovieReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'review', 'user', 'movie', 'likes', 'posted', 'edited')
    list_filter = ('movie', 'posted', 'likes', 'user', 'edited')
    ordering = ('movie', 'posted', 'edited', 'likes')
    save_on_top = True
    search_fields = ('review', )


@admin.register(MovieRatings)
class MovieRatingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'user', 'movie', 'posted', 'edited')
    list_filter = ('movie', 'posted', 'user', 'edited', 'rating')
    ordering = ('movie', 'posted', 'rating', 'edited')
    save_on_top = True


@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name', )
    ordering = ('name', )
    save_on_top = True
    search_fields = ('name', )


@admin.register(MovieCharacters)
class MovieCharactersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'movie', 'celebrity')
    list_filter = ('movie', 'celebrity')
    ordering = ('name', 'movie', 'celebrity')
    save_on_top = True
    search_fields = ('name', )


@admin.register(PlannedMovies)
class PlannedMoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'movie')
    list_filter = ('user', 'movie')
    ordering = ('user', 'movie')
    save_on_top = True
    search_fields = ('movie', )


@admin.register(MovieReviewLikes)
class MovieReviewLikesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'review', 'posted')
    list_filter = ('user', 'review', 'posted')
    ordering = ('user', 'review')
    save_on_top = True
