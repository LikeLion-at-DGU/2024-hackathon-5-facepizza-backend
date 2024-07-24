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
from .models import DailyChallenge
from .serializers import DailyChallengeSerializer

class DailyChallengeCreateView(generics.CreateAPIView):
    serializer_class = DailyChallengeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

