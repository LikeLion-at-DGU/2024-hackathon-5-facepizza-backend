from rest_framework import serializers
from .models import *

class MissonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mission
        fields = '__all__'
        read_only_fields = ['user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MypageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'