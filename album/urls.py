from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import EmotionImageListViewSet, EmotionImageViewSet

from django.conf import settings
from django.conf.urls.static import static

app_name = 'album'

router = SimpleRouter(trailing_slash=False)
router.register(r'albums', EmotionImageListViewSet, basename='albums')
router.register(r'images', EmotionImageViewSet, basename='images')

urlpatterns = [
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
