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
from .views import ExerciseRecordCreateView

urlpatterns = [
    path('stretching/record/', ExerciseRecordCreateView.as_view(), name='exercise_record_create'),
]
