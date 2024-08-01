from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action

from .permissions import IsOwnerOrReadOnly
from .models import EmotionImage
from character.models import Character
from .serializers import EmotionImageSerializer

from django.shortcuts import get_object_or_404

# Create your views here.
class EmotionImageCreateViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = EmotionImage.objects.all()
    serializer_class = EmotionImageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        try:
            character = Character.objects.get(user=self.request.user)
        except Character.DoesNotExist:
            return Response({'error': 'Character not found'}, status=404)
        
        character.update_experience(5)