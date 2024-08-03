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

from snap.models import EmotionImage
from tracking.models import Report

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
    
    @action(detail=False, methods=['get']) # 새로운 엔드포인트 'totalnum'
    def totalnum(self, request):
        user = request.user
        
        # emotion_counts : 사용자가 가진 EmotionImage 객체(각 감정별 사진)의 개수
        emotions = ['happy', 'surprised', 'angry', 'sad', 'neutral', 'fearful', 'disgusted']
        emotion_counts = {emotion: EmotionImage.objects.filter(user=user, emotion=emotion).count() for emotion in emotions}

        # 최신 트래킹 보고서를 가져옴
        reports = Report.objects.filter(user=user).last()  # 사용자의 최신 report 객체
        if not reports:
            return Response({"error": "No tracking report found."}, status=400)

        # 트래킹 보고서에서 감정비율 추출
        emotion_ratios = {
            'happy': reports.happy_ratio,
            'surprised': reports.surprised_ratio,
            'angry': reports.angry_ratio,
            'sad': reports.sad_ratio,
            'neutral': reports.neutral_ratio,
            'fearful': reports.fearful_ratio,
            'disgusted': reports.disgusted_ratio
        }

        # 감정별 총 점수 계산
        total_points = {
            'happy': emotion_counts['happy'] * 5 + emotion_ratios['happy'] * 10,
            'surprised': emotion_counts['surprised'] * 5 + emotion_ratios['surprised'] * 10,
            'angry': emotion_counts['angry'] * 5 + emotion_ratios['angry'] * 10,
            'sad': emotion_counts['sad'] * 5 + emotion_ratios['sad'] * 10,
            'neutral': emotion_ratios['neutral'] * 10,
            'fearful': emotion_ratios['fearful'] * 10,
            'disgusted': emotion_ratios['disgusted'] * 10
        }

        # 각 감정별 점수 반환
        return Response({
            'total_points': total_points
        })
