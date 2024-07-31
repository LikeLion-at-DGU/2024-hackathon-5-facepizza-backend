from rest_framework import serializers
from .models import Report
import base64
import uuid
from django.core.files.base import ContentFile

class ReportSerializer(serializers.ModelSerializer):
    highlights = serializers.ListField(child=serializers.DictField(), write_only=True, required=False)

    class Meta:
        model = Report
        fields = '__all__'

    # creat 함수 오버라이딩
    def create(self, validated_data):
        highlights = validated_data.pop('highlights', [])
        report = super().create(validated_data)

        # 이미지 디코딩
        try:
            for highlight in highlights:
                image_data = highlight.get('image')
                emotion = highlight.get('emotion')
                if image_data:
                    format, imgstr = image_data.split(';base64,') 
                    ext = format.split('/')[-1] 
                    imgstr = base64.b64decode(imgstr)
                    file_name = f"{uuid.uuid4()}.{ext}"
                    image_file = ContentFile(imgstr, name=file_name)

                    if ext not in ['jpg', 'jpeg', 'png']:
                        raise serializers.ValidationError("Unsupported file type")

                    if emotion == 'happy':
                        report.happy_highlight = image_data
                    elif emotion == 'sad':
                        report.sad_highlight = image_data
                    elif emotion == 'angry':
                        report.angry_highlight = image_data
                    elif emotion == 'surprised':
                        report.surprised_highlight = image_data
                    elif emotion == 'disgusted':
                        report.disgusted_highlight = image_data
                    elif emotion == 'fearful':
                        report.fearful_highlight = image_data
                    elif emotion == 'neutral':
                        report.neutral_highlight = image_data

            report.save()
        except Exception as e:
            raise serializers.ValidationError({"error": str(e)})

        return report