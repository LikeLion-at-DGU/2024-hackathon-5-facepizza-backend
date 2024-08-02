from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action
from django.contrib.auth.models import User

from .permissions import IsOwnerOrReadOnly
from .serializers import MypageSerializer
from character.serializers import CharacterSerializer
from character.models import Character

from django.shortcuts import get_object_or_404

# Create your views here.
class MypageViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = MypageSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # 인증된 사용자의 객체를 반환
        return self.request.user

    @action(detail=False, methods=['get'])
    def profile(self, request, *args, **kwargs):
        user = self.get_object()
        user_serializer = MypageSerializer(user)

        # 사용자의 캐릭터 정보를 가져옵니다
        characters = Character.objects.filter(user=user)
        character_serializer = CharacterSerializer(characters, many=True)

        # 응답 데이터에 사용자 정보와 캐릭터 정보를 포함시킵니다
        return Response({
            'user': user_serializer.data,
            'characters': character_serializer.data
        })
