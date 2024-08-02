from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from tracking.models import Report
from .models import Character
from .serializers import CharacterSerializer
from tracking.serializers import ReportSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    @action(detail=True, methods=['get'])
    def tracking_time(self, request, pk=None):
        try:
            character = self.get_object()
            user = character.user
        except Character.DoesNotExist:
            return Response({'error': 'Character not found'}, status=404)

        reports = Report.objects.filter(user=user)
        total_time = sum([(report.ended_at - report.created_at).total_seconds() for report in reports])

        exp_increment = int(total_time // 60)
        if exp_increment > 0:
            character.update_experience(exp_increment)

        report_serializer = ReportSerializer(reports, many=True)

        return Response({
            'total_time_minutes': total_time // 60,
            'reports': report_serializer.data,
            'level': character.level,
            'experience': character.exp
        })
