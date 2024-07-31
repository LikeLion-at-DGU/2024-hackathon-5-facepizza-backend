from django.db import models
from django.contrib.auth.models import User

# Create your models here.

EMOTION_CHOICES = [
    ('happy', 'Happy'),
    ('sad', 'Sad'),
    ('angry', 'Angry'),
    ('surprised', 'Surprised'),
    ('disgusted', 'Disgusted'),
    ('fearful', 'Fearful'),
    ('neutral', 'Neutral'),
]

class Mission(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=50, choices=EMOTION_CHOICES)
    goal_count = models.PositiveIntegerField()
    now_count = models.PositiveIntegerField(default=0)
    experience = models.PositiveIntegerField()
    is_completed = models.PositiveIntegerField(default=0) #0:False, 1:True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
