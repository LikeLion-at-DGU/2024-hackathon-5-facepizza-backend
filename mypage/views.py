from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action

from .permissions import IsOwnerOrReadOnly
from .models import Achievement
from .serializers import AchievementSerializer, UserSerializer

from django.shortcuts import get_object_or_404

# Create your views here.
class MypageViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class AchievementViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = AchievementSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Achievement.objects.filter(user=self.request.user.id)