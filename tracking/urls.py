from django.urls import path, include
from rest_framework import routers
from .views import ReportViewSet

from django.conf.urls.static import static
from django.conf import settings

app_name = 'tracking'

default_router = routers.SimpleRouter(trailing_slash=False)
default_router.register("report", ReportViewSet, basename="report")

urlpatterns = [
    path("", include(default_router.urls)),
]   + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)