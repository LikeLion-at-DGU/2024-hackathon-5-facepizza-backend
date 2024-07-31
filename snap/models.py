from django.db import models
from django.contrib.auth.models import User
import os
from django.core.files.storage import default_storage
from django.db.models.signals import post_delete
from django.dispatch import receiver

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

class EmotionImage(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.TextField()
    emotion = models.CharField(max_length=50, choices=EMOTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)