from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def HighlightImage_upload_path(instance, filename):
    return f'{instance.pk}/{filename}'

EMOTION_CHOICES = [
    ('happy', 'Happy'),
    ('sad', 'Sad'),
    ('angry', 'Angry'),
    ('surprised', 'Surprised'),
    ('disgusted', 'Disgusted'),
    ('fearful', 'Fearful'),
    ('neutral', 'Neutral'),
]

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    # user_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    happy = models.FloatField(default=0)
    sad = models.FloatField(default=0)
    angry = models.FloatField(default=0)
    surprised = models.FloatField(default=0)
    disgusted = models.FloatField(default=0)
    fearful = models.FloatField(default=0)
    neutral = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50, null=True)
    happy_highlight = models.TextField(blank=True)
    sad_highlight = models.TextField(blank=True)
    angry_highlight = models.TextField(blank=True)
    surprised_highlight = models.TextField(blank=True)
    disgusted_highlight = models.TextField(blank=True)
    fearful_highlight = models.TextField(blank=True)
    neutral_highlight = models.TextField(blank=True)