from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CharacterViewSet

router = DefaultRouter()
router.register(r'characters', CharacterViewSet, basename='character')

urlpatterns = [
    path('', include(router.urls)),
    path('characters/tracking_time', CharacterViewSet.as_view({'get': 'tracking_time'}), name='character-tracking-time')
]
