from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Celebrity)
class CelebrityAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name', 'bio', 'get_image', 'birth_date')
    list_display_links = ('name',)
    ordering = ('name', 'id', 'birth_date')
    search_fields = ('name', 'bio')
    list_filter = ('birth_date', )
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=70 style='border-radius: 10px;'>")


@admin.register(CelebrityPhotos)
class CelebrityPhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'celebrity', 'get_photo')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=70 style='border-radius: 10px;'>")


@admin.register(CelebrityVideos)
class CelebrityVideosAdmin(admin.ModelAdmin):
    list_display = ('id', 'celebrity', 'get_video')

    def get_video(self, obj):
        if obj.video:
            return mark_safe(f"<video src='{obj.video.url}' width=70 style='border-radius: 10px;'>")


@admin.register(CelebrityOccupations)
class CelebrityOccupationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name', )
    ordering = ('name', )


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name', )
    ordering = ('name', )
