from rest_framework import serializers
from .models import *

class HighlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Highlight
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    highlights = HighlightSerializer(many=True, read_only=True)

    class Meta:
        model = Report
        fields = '__all__'