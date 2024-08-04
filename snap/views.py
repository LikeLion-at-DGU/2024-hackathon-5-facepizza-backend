from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action

from .permissions import IsOwnerOrReadOnly
from .models import EmotionImage
from character.models import Character
from .serializers import EmotionImageSerializer

from django.shortcuts import get_object_or_404
import base64
from django.core.files.base import ContentFile

# Create your views here.
class EmotionImageCreateViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = EmotionImage.objects.all()
    serializer_class = EmotionImageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)

        # 이미지 디코딩
        image_data = self.request.data.get('image')
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        instance.image.save(f'{instance.id}.{ext}', ContentFile(base64.b64decode(imgstr)), save=False)
        instance.save()

        try:
            character = Character.objects.get(user=self.request.user)
        except Character.DoesNotExist:
            return Response({'error': 'Character not found'}, status=404)
        
        character.update_experience(5)