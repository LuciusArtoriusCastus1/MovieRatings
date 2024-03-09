from django.urls import path, include
from rest_framework import routers

from celebrities.documents import CelebritiesDocumentViewSet
from celebrities.views import *

router = routers.DefaultRouter()
router.register(r'celebrities', CelebritiesViewSet, basename='celebrities')

router1 = routers.DefaultRouter()
router1.register(r'countries', CountriesViewSet, basename='countries')

router2 = routers.DefaultRouter()
router2.register(r'occupations', CelebrityOccupationsViewSet, basename='occupations')

router3 = routers.DefaultRouter()
router3.register(r'searchcelebrities', CelebritiesDocumentViewSet, basename='searchcelebrities')


urlpatterns = [
    path('celebrities/photo/create/', CelebrityPhotosCreate.as_view(), name='celeb_photo_create'),
    path('celebrities/photo/delete/<int:pk>/', CelebrityPhotosDestroy.as_view(), name='celeb_photo_del'),
    path('celebrities/video/create/', CelebrityVideosCreate.as_view(), name='celeb_video_create'),
    path('celebrities/video/delete/<int:pk>/', CelebrityVideosDestroy.as_view(), name='celeb_video_del'),

    path('', include(router.urls)),
    path('', include(router1.urls)),
    path('', include(router2.urls)),
    path('', include(router3.urls)),
]
