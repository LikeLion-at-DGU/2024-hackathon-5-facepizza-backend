from rest_framework import serializers
from .models import *
import base64
from django.core.files.base import ContentFile

class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            # base64 encoded image
            format, imgstr = data.split(';base64,') 
            ext = format.split('/')[-1] 
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super(Base64ImageField, self).to_internal_value(data)

class EmotionImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(max_length=None, use_url=True,)

    class Meta:
        model = EmotionImage
        fields = '__all__'
        read_only_fields = ['user']
