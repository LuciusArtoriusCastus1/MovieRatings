from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import User, Genders


@admin.register(User)
class UserConfig(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'get_avatar', 'gender', 'join_date', 'is_staff',)
    list_display_links = ('name',)
    ordering = ('name', 'join_date')
    search_fields = ('name', 'bio')
    list_editable = ('is_staff', )
    list_filter = ('is_active', 'is_staff', 'join_date')
    readonly_fields = ('join_date',)
    save_on_top = True

    def get_avatar(self, obj):
        if obj.avatar:
            return mark_safe(f"<img src='{obj.avatar.url}' width=70 style='border-radius: 100px;'>")

    get_avatar.short_description = 'Avatar'


@admin.register(Genders)
class GendersConfig(admin.ModelAdmin):
    list_display = ('gender', )

