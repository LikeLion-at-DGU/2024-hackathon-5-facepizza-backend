# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import EmotionRecordViewSet

# app_name = 'stretching'

# router = DefaultRouter()
# router.register(r'emotion-records', EmotionRecordViewSet, basename='emotionrecord')

# urlpatterns = [
#     path("", include(router.urls)),
# ]

# stretching/urls.py
from django.urls import path
from .views import DailyChallengeCreateView

urlpatterns = [
    path('stretching/record/', DailyChallengeCreateView.as_view(), name='daily_challenge_create'),
]
