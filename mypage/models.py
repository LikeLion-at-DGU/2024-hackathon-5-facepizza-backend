from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ACHIEVEMENT_CHOICES = [
    ('3days_stretching', '3days_stretching'),
    ('7days_stretching', '7days_stretching'),
    ('30days_stretching', '30days_stretching'),
    ('3days_practicing', '3days_practicing'),
    ('7days_practicing', '7days_practicing'),
    ('30days_practicing', '30days_practicing'),
]

class Achievement(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, choices = ACHIEVEMENT_CHOICES)
    content = models.TextField()
    isComplete = models.PositiveIntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)