from rest_framework import serializers
from .models import *

class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        fields = '__all__'
        read_only_fields = ['user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'