from django.urls import path, include
from rest_framework import routers
from .views import EmotionImageListViewSet, EmotionImageViewSet

from django.conf import settings
from django.conf.urls.static import static

app_name = 'album'

default_router = routers.SimpleRouter(trailing_slash=False)
default_router.register("album", EmotionImageListViewSet, basename="album")

emotion_image_router = routers.SimpleRouter(trailing_slash=False)
emotion_image_router.register("image", EmotionImageViewSet, basename="image")

urlpatterns = [
    path('', include(default_router.urls)),
    path('album/', include(emotion_image_router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)