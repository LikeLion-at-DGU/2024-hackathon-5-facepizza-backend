from rest_framework import serializers
from .models import *

class EmotionImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmotionImage
        fields = '__all__'
        read_only_fields = ['user']