from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action

from .permissions import IsOwnerOrReadOnly
from .models import EmotionImage
from .serializers import EmotionImageSerializer

from django.shortcuts import get_object_or_404

# Create your views here.
class EmotionImageCreateViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = EmotionImage.objects.all()
    serializer_class = EmotionImageSerializer
    permissions_classes = [IsAuthenticated]