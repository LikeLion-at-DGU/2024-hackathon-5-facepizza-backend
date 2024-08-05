from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action

from .permissions import IsOwnerOrReadOnly
from snap.models import EmotionImage
from snap.serializers import EmotionImageSerializer

from django.shortcuts import get_object_or_404

from django.utils import timezone
from datetime import timedelta

# Create your views here.
class EmotionImageListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = EmotionImageSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = EmotionImage.objects.all()
        emotion = self.request.query_params.get('emotion')
        
        if emotion:
            queryset = queryset.filter(emotion=emotion)
        
        return queryset.filter(user=self.request.user.id)
    
    @action(detail=False, methods=['get'], url_path='count')
    def count_today(self, request):
        now = timezone.now()
        start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
        count = EmotionImage.objects.filter(
            user=self.request.user.id,
            created_at__gte=start_of_day
        ).count()
        return Response({'count': count})

class EmotionImageViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    queryset = EmotionImage.objects.all()
    serializer_class = EmotionImageSerializer
    permission_classes = [IsAuthenticated]