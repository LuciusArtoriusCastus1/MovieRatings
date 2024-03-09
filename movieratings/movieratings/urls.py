from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as yasg_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('celebrities.urls')),
    path('', include('movies.urls')),
    path('', include('custom_user.urls')),
    path('', include('tv_shows.urls')),

    path('social/auth/', include('drf_social_oauth2.urls', namespace='drf')),

    path('djoser/auth/', include('djoser.urls')),
    path('token/auth/', include('djoser.urls.authtoken')),
    path('jwt/auth/', include('djoser.urls.jwt')),
    path('api-auth/', include('rest_framework.urls')),

]

urlpatterns += yasg_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

