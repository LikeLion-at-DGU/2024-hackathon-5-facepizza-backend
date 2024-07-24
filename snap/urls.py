from django.urls import path, include
from rest_framework import routers
from .views import EmotionImageCreateViewSet

from django.conf import settings
from django.conf.urls.static import static

app_name = 'snap'

default_router = routers.SimpleRouter(trailing_slash=False)
default_router.register("snaps", EmotionImageCreateViewSet, basename="snaps")

urlpatterns = [
    path("", include(default_router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)