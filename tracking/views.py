from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Report
from .serializers import ReportSerializer
from rest_framework.exceptions import NotFound

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        report = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get_queryset(self):
        user = self.request.user
        return Report.objects.filter(user=user)

    def retrieve(self, request, *args, **kwargs):
        try:
            report = self.get_queryset().get(pk=kwargs['pk'])
        except Report.DoesNotExist:
            raise NotFound(detail="Report not found", code=404)
        serializer = self.get_serializer(report)
        return Response(serializer.data)