from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from django.core.files.base import ContentFile

from .models import Report, Highlight
from .serializers import ReportSerializer, HighlightSerializer

from django.shortcuts import get_object_or_404
import base64

# Create your views here.
# report CRUD
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

# highlight CRUD
class HighlightViewSet(viewsets.ModelViewSet):
    queryset = Highlight.objects.all()
    serializer_class = HighlightSerializer

    # create 오버라이딩
    def create(self, request, *args, **kwargs):
        data = request.data
        report_id = data.get("report_id")
        report = get_object_or_404(Report, id=report_id)
        emotion = data.get("emotion")

        # 하이라이드 사진 base64 디코딩
        # 이미지 전송 방식 조금 더 찾아보기
        image_data = data.get("image")
        format, imgstr = image_data.split(";base64,")
        ext = format.split('/')[-1]
        image = ContentFile(base64.b64decode(imgstr), name=f'{emotion}.{ext}')

        highlight = Highlight.objects.create(
            report_id = report,
            image = image,
            emotion  = emotion
        )

        serializer = self.get_serializer(highlight)
        return Response(serializer.data)