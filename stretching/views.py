# from django.shortcuts import render
# from rest_framework import viewsets, mixins
# from rest_framework.permissions import IsAuthenticated
# from .models import EmotionRecord
# from .serializers import EmotionRecordSerializer
# # Create your views here.

# class EmotionRecordViewSet(viewsets.GenericViewSet, 
#                            mixins.CreateModelMixin, mixins.ListModelMixin):
#     serializer_class = EmotionRecordSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         # 모든 감정 기록 & url 쿼리 파라미터에서 emotion 값 가져오기
#         queryset = EmotionRecord.objects.all()
#         emotion = self.request.query_params.get('emotion')

#         # 해당 감정과 score이 0.7보다 큰 경우만 필터링
#         if emotion:
#             queryset = queryset.filter(emotion=emotion, score__gt=0.7)

#         # 인증된 사용자만 조회 가능
#         return queryset.filter(user=self.request.user)
    
#     # 새로운 EmotionRecord 인스턴스를 생성할 때 호출됨.
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# stretching/views.py
from rest_framework import generics, permissions
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import get_object_or_404

from .models import DailyChallenge
from mypage.models import Achievement
from .serializers import DailyChallengeSerializer
from mypage.serializers import AchievementSerializer

class DailyChallengeCreateView(generics.CreateAPIView):
    serializer_class = DailyChallengeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        self.check_achievement()
    
    def check_achievement(self):
        user = self.request.user

        if Achievement.objects.filter(user=user, title="30days_stretching", isComplete=0):
            self.update_achievement(30, "stretching", user)

        if Achievement.objects.filter(user=user, title="7days_stretching", isComplete=0):
            self.update_achievement(7, "stretching", user)

        if Achievement.objects.filter(user=user, title="3days_stretching", isComplete=0):
            self.update_achievement(3, "stretching", user)

        if Achievement.objects.filter(user=user, title="30days_practicing", isComplete=0):
            self.update_achievement(30, "practicing", user)
        
        if Achievement.objects.filter(user=user, title="7days_practicing", isComplete=0):
            self.update_achievement(7, "practicing", user)

        if Achievement.objects.filter(user=user, title="3days_practicing", isComplete=0):
            self.update_achievement(3, "practicing", user)

    def update_achievement(self, goal_date, goal_title, user):
        today = timezone.now().date()
        # 최근 goal_date일간의 DailyChallenge를 확인
        challenges = DailyChallenge.objects.filter(
            user=user,
            content=goal_title,
            created_at__date__gte=today - timedelta(days=(goal_date-1))
        ).values_list('created_at', flat=True)

        # 날짜 리스트 생성
        challenge_dates = [challenge.date() for challenge in challenges]

        # 연속된 goal_date일이 있는지 확인
        consecutive_days = all(
            (today - timedelta(days=i)) in challenge_dates for i in range(goal_date)
        )
        print(consecutive_days)
        if consecutive_days:
            # Achievement 업데이트
            title = str(goal_date)+"days_"+str(goal_title)
            Achievement.objects.filter(user=user, title=title, isComplete=False).update(isComplete=1)
        