from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from tracking.models import Report
from .models import Character
from .serializers import CharacterSerializer
from tracking.serializers import ReportSerializer
from datetime import timedelta
from zoneinfo import ZoneInfo
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotAuthenticated

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    @action(detail=False, methods=['get'], url_path='tracktime')
    def tracking_time(self, request):
        if not request.user.is_authenticated:
            raise NotAuthenticated("Authentication credentials were not provided or are invalid.")
        
        try:
            user = request.user
            character = Character.objects.get(user=user)
        except Character.DoesNotExist:
            return Response({'error': 'Character not found'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

        reports = Report.objects.filter(user=user)
        daily_time = {}
        total_time_seconds = 0

        # KST timezone
        kst = ZoneInfo('Asia/Seoul')

        for report in reports:
            start_time = report.created_at.replace(tzinfo=ZoneInfo('UTC')).astimezone(kst)
            end_time = report.ended_at.replace(tzinfo=ZoneInfo('UTC')).astimezone(kst)

            current_start = start_time
            while current_start.date() <= end_time.date():
                next_midnight = (current_start + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
                if end_time < next_midnight:
                    duration = end_time - current_start
                else:
                    duration = next_midnight - current_start

                day = current_start.date().isoformat()
                if day not in daily_time:
                    daily_time[day] = 0
                daily_time[day] += duration.total_seconds()

                current_start = next_midnight

        for day, seconds in daily_time.items():
            total_time_seconds += seconds
            minutes, seconds = divmod(seconds, 60)
            daily_time[day] = {'minutes': int(minutes), 'seconds': int(seconds), 'total_seconds': int(seconds + minutes * 60)}

        minutes, seconds = divmod(total_time_seconds, 60)
        exp_increment = int(total_time_seconds // 60)
        if exp_increment > 0:
            character.update_experience(exp_increment)

        report_serializer = ReportSerializer(reports, many=True)

        # Convert report times to KST
        reports_data = []
        for report_data in report_serializer.data:
            report_obj = Report.objects.get(id=report_data['id'])
            created_at_kst = report_obj.created_at.replace(tzinfo=ZoneInfo('UTC')).astimezone(kst)
            ended_at_kst = report_obj.ended_at.replace(tzinfo=ZoneInfo('UTC')).astimezone(kst)
            report_data['created_at'] = created_at_kst
            report_data['ended_at'] = ended_at_kst
            report_data['title'] = created_at_kst.strftime('%Y-%m-%d %H:%M:%S')
            reports_data.append(report_data)

        return Response({
            'total_time_minutes': int(minutes),
            'total_time_seconds': int(total_time_seconds),
            'total_time': f"{int(minutes)}분 {int(seconds)}초",
            'daily_time': daily_time,
            'reports': reports_data,
            'level': character.level,
            'experience': character.exp
        })
