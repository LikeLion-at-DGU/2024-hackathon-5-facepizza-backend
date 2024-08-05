from rest_framework import serializers
from .models import *
import base64
from django.core.files.base import ContentFile

class EmotionImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmotionImage
        fields = '__all__'
        read_only_fields = ['user']
