# from rest_framework import serializers
# from .models import EmotionRecord

# class EmotionRecordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EmotionRecord
#         fields = ['id', 'user', 'emotion', 'score', 'timestamp']
#         read_only_fields = ['user', 'timestamp']
        
# stretching/serializers.py
from rest_framework import serializers
from .models import DailyChallenge

class DailyChallengeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  
    # user 필드를 username으로 직렬화

    class Meta:
        model = DailyChallenge
        fields = '__all__'
        read_only_fields = ['user']
