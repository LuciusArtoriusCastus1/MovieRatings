from django.contrib import admin
from django.utils.safestring import mark_safe

from tv_shows.models import TVShowCharacters, PlannedTVShows, TVShowRatings, TVShowReviews, TVShowVideos, TVShowPhotos, \
    TVShow, TVEpisodes, TVEpisodePhotos, TVEpisodeVideos, TVEpisodeReviews, TVEpisodeRatings, TVShowReviewLikes, \
    TVEpisodeReviewLikes


@admin.register(TVShow)
class TVShowAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'release_start_date', 'rating', 'country', 'budget', 'box_office')
    search_fields = ('name', 'slug', 'description')
    list_filter = ('name', 'release_start_date', 'rating', 'country', 'budget', 'box_office')
    ordering = ('name', 'release_start_date', 'posted', 'edited', 'rating', 'budget', 'box_office')
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    readonly_fields = ('rating', )


@admin.register(TVShowPhotos)
class TVShowPhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'tv_show', 'get_photo')
    list_filter = ('tv_show', )
    ordering = ('tv_show', )
    save_on_top = True
    search_fields = ('tv_show', )

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=70 style='border-radius: 10px;'>")


@admin.register(TVShowVideos)
class TVShowVideosAdmin(admin.ModelAdmin):
    list_display = ('id', 'tv_show', 'get_video')
    list_filter = ('tv_show',)
    ordering = ('tv_show',)
    save_on_top = True
    search_fields = ('tv_show',)

    def get_video(self, obj):
        if obj.video:
            return mark_safe(f"<video src='{obj.video.url}' width=70 style='border-radius: 10px;'>")


@admin.register(TVShowReviews)
class TVShowReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'review', 'user', 'likes', 'tv_show', 'posted', 'edited')
    list_filter = ('tv_show', 'posted', 'user', 'edited', 'likes')
    ordering = ('tv_show', 'posted', 'edited', 'likes')
    save_on_top = True
    search_fields = ('review', )


@admin.register(TVShowRatings)
class TVShowRatingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'user', 'tv_show', 'posted', 'edited')
    list_filter = ('tv_show', 'posted', 'user', 'edited', 'rating')
    ordering = ('tv_show', 'posted', 'rating', 'edited')
    save_on_top = True


@admin.register(TVShowCharacters)
class TVShowCharactersAdmin(admin.ModelAdmin):
    list_display = ('id', 'tv_show', 'tv_show', 'celebrity')
    list_filter = ('tv_show', 'celebrity')
    ordering = ('name', 'tv_show', 'celebrity')
    save_on_top = True
    search_fields = ('name', )


@admin.register(PlannedTVShows)
class PlannedTVShowsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'tv_show')
    list_filter = ('user', 'tv_show')
    ordering = ('user', 'tv_show')
    save_on_top = True
    search_fields = ('tv_show', )



@admin.register(TVEpisodes)
class TVEpisodesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'release_date', 'tv_show', 'rating')
    search_fields = ('name', 'slug', 'description')
    list_filter = ('name', 'release_date', 'rating')
    ordering = ('name', 'release_date', 'posted', 'edited', 'rating',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    readonly_fields = ('rating', )


@admin.register(TVEpisodePhotos)
class TVEpisoddePhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'tv_episode', 'get_photo')
    list_filter = ('tv_episode', )
    ordering = ('tv_episode', )
    save_on_top = True
    search_fields = ('tv_episode', )

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=70 style='border-radius: 10px;'>")


@admin.register(TVEpisodeVideos)
class TVEpisodeVideosAdmin(admin.ModelAdmin):
    list_display = ('id', 'tv_episode', 'get_video')
    list_filter = ('tv_episode',)
    ordering = ('tv_episode',)
    save_on_top = True
    search_fields = ('tv_episode',)

    def get_video(self, obj):
        if obj.video:
            return mark_safe(f"<video src='{obj.video.url}' width=70 style='border-radius: 10px;'>")


@admin.register(TVEpisodeReviews)
class TVEpisodeReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'review', 'user', 'tv_episode', 'likes', 'posted', 'edited')
    list_filter = ('tv_episode', 'posted', 'likes', 'user', 'edited')
    ordering = ('tv_episode', 'posted', 'edited', 'likes')
    save_on_top = True
    search_fields = ('review', )


@admin.register(TVEpisodeRatings)
class TVEpisodeRatingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'user', 'tv_episode', 'posted', 'edited')
    list_filter = ('tv_episode', 'posted', 'user', 'edited', 'rating')
    ordering = ('tv_episode', 'posted', 'rating', 'edited')
    save_on_top = True


@admin.register(TVShowReviewLikes)
class TVShowReviewLikesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'review', 'posted')
    list_filter = ('user', 'review', 'posted')
    ordering = ('user', 'review')
    save_on_top = True


@admin.register(TVEpisodeReviewLikes)
class TVEpisodeReviewLikesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'review', 'posted')
    list_filter = ('user', 'review', 'posted')
    ordering = ('user', 'review')
    save_on_top = True
